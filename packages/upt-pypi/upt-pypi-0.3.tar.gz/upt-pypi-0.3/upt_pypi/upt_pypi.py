# Copyright 2018      Cyril Roelandt
#
# Licensed under the 3-clause BSD license. See the LICENSE file.
import json
import pkg_resources
import re
import tarfile
import tempfile
from urllib.request import urlretrieve
import zipfile

import requests
import upt


class PyPIPackage(upt.Package):
    pass


class PyPIFrontend(upt.Frontend):
    name = 'pypi'

    @staticmethod
    def get_archive_info(release, kind):
        for elt in release:
            if elt['packagetype'] == kind:
                digests = elt.get('digests', {})
                return (elt['url'], elt.get('size', 0),
                        digests.get('md5'), digests.get('sha256'))
        raise ValueError(f'No archive of type "{kind}" could be found')

    def get_sdist_archive_url(self, release):
        url, _, _, _ = self.get_archive_info(release, 'sdist')
        return url

    def get_wheel_url(self, release):
        url, _, _, _ = self.get_archive_info(release, 'bdist_wheel')
        return url

    @staticmethod
    def _string_req_to_upt_pkg_req(string_req):
        r = pkg_resources.Requirement.parse(string_req)
        name = r.project_name
        specifier = ','.join(op+version for (op, version) in r.specs)
        return upt.PackageRequirement(name, specifier)

    @classmethod
    def _string_req_list_to_upt_pkg_req_list(cls, string_req_list):
        return [cls._string_req_to_upt_pkg_req(s) for s in string_req_list]

    @classmethod
    def compute_requirements_from_metadata_json(cls, json_file):
        requirements = {}
        parse_method = cls._string_req_list_to_upt_pkg_req_list
        try:
            with open(json_file) as f:
                j = json.load(f)
                for reqs in j.get('run_requires', []):
                    if list(reqs.keys()) != ['requires']:
                        continue
                    requirements['run'] = parse_method(reqs['requires'])
                for reqs in j.get('test_requires', []):
                    if list(reqs.keys()) != ['requires']:
                        continue
                    requirements['test'] = parse_method(reqs['requires'])
        except json.JSONDecodeError:
            return {}

        return requirements

    @classmethod
    def compute_requirements_from_wheel(cls, wheel_url):
        with tempfile.NamedTemporaryFile() as wheel,\
             tempfile.TemporaryDirectory() as d:
            urlretrieve(wheel_url, wheel.name)
            dirname = '-'.join(wheel_url.rsplit('/', 1)[-1].split('-', 2)[:2])
            dirname += '.dist-info'
            z = zipfile.ZipFile(wheel.name)
            try:
                z.extract(f'{dirname}/metadata.json', d)
                return cls.compute_requirements_from_metadata_json(
                    f'{d}/{dirname}/metadata.json')
            except KeyError:
                # No metadata.json in this wheel
                return {}

    def compute_requirements(self):
        """Computes the requirements using various methods.

        Try to compute the requirements of the package by;
        - looking at the requires_dist field of the JSON document we are
          parsing.
        - downloading and opening the wheel from this release, then reading the
          metadata.json file inside.
        """
        reqs = {}
        run_reqs = []
        test_reqs = []
        for req in self.json.get('info', {}).get('requires_dist', []) or []:
            try:
                req_name, extra = req.split(';')
                extra = extra.strip()
            except ValueError:
                # No "extras".
                req_name = req
                extra = None

            pkg = self._string_req_to_upt_pkg_req(req_name)
            if extra is not None:
                # We only care about extras if they are likely to define the
                # test requirements.
                # TODO: care about optional runtime requirements when upt
                # provides support for them.
                # TODO: handle cases where 'extra' matches a requirement on the
                # Python version.
                m = re.match("extra == '(.*)'", extra)
                if m:
                    extra_name = m.group(1)
                    if extra_name in ('test', 'tests', 'testing'):
                        test_reqs.append(pkg)
            else:
                run_reqs.append(pkg)

        if run_reqs and test_reqs:
            # We got both the runtime and test requirements.
            reqs['run'] = run_reqs
            reqs['test'] = test_reqs
        else:
            # We probably missed some of the requirements, let's see whether
            # we are more lucky with the wheel.
            try:
                version = self.json['info']['version']
                wheel_url = self.get_wheel_url(self.json['releases'][version])
                wheel_reqs = self.compute_requirements_from_wheel(wheel_url)
            except ValueError:
                # No wheel for this package.
                wheel_reqs = {}
            finally:
                run_reqs = run_reqs or wheel_reqs.get('run')
                test_reqs = test_reqs or wheel_reqs.get('test')
                if run_reqs:
                    reqs['run'] = run_reqs
                if test_reqs:
                    reqs['test'] = test_reqs

        return reqs

    def guess_licenses(self, release):
        """Try to guess the license(s) used by the package.

        There may be more than one license that applies, which is why we return
        a list.

        The package classifiers should give us the info we need, but:
        - they may not be precise enough (no distinction between 2-clause BSD
          and 3-clause BSD, for instance);
        - the author of the packge may not have added the relevant classifiers.

        The "license" field of setup.py ends up in a file called metadata.json,
        available in the wheel archive. This is a user-defined string though,
        so there is no standard to refer to licenses. We will therefore not use
        it. We may want to try and check the LICENSE file distributed with the
        source code.
        """
        # All available license classifiers provided by PyPI.
        # TODO: Update the list once
        # https://github.com/pypa/warehouse/issues/2996 has been fixed.
        all_license_classifiers = {
            'License :: Aladdin Free Public License (AFPL)':
                upt.licenses.AladdinFreePublicLicense,
            'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication':
                upt.licenses.CC0LicenceOneDotZero,
            'License :: CeCILL-B Free Software License Agreement (CECILL-B)':
                upt.licenses.CeCILLBLicense,
            'License :: CeCILL-C Free Software License Agreement (CECILL-C)':
                upt.licenses.CeCILLCLicense,
            'License :: Eiffel Forum License (EFL)':
                upt.licenses.EiffelForumLicenseTwoDotZero,
            'License :: Nokia Open Source License (NOKOS)':
                upt.licenses.NokiaOpenSourceLicense,
            'License :: OSI Approved :: Attribution Assurance License':
                upt.licenses.AttributionAssuranceLicense,
            'License :: OSI Approved :: Boost Software License 1.0 (BSL-1.0)':
                upt.licenses.BoostSoftwareLicense,
            'License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)': # noqa
                upt.licenses.CeCILLTwoDotOne,
            'License :: OSI Approved :: Common Development and Distribution License 1.0 (CDDL-1.0)': # noqa
                upt.licenses.CommonDevelopmentAndDistributionLicenseOneDotZero,
            'License :: OSI Approved :: Common Public License':
                upt.licenses.CommonPublicLicenseOneDotZero,
            'License :: OSI Approved :: Eclipse Public License 1.0 (EPL-1.0)':
                upt.licenses.EclipsePublicLicenseOneDotZero,
            'License :: OSI Approved :: Eiffel Forum License':
                upt.licenses.EiffelForumLicenseTwoDotZero,
            'License :: OSI Approved :: European Union Public Licence 1.0 # (EUPL 1.0)': # noqa
                upt.licenses.EuropeanUnionPublicLicenseOneDotZero,
            'License :: OSI Approved :: European Union Public Licence 1.1 (EUPL 1.1)': # noqa
                upt.licenses.EuropeanUnionPublicLicenseOneDotOne,
            'License :: OSI Approved :: GNU Affero General Public License v3':
                upt.licenses.GNUAfferoGeneralPublicLicenseThreeDotZero,
            'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)': # noqa
                upt.licenses.GNUAfferoGeneralPublicLicenseThreeDotZeroPlus,
            'License :: OSI Approved :: GNU General Public License v2 (GPLv2)':
                upt.licenses.GNUGeneralPublicLicenseTwo,
            'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)': # noqa
                upt.licenses.GNUGeneralPublicLicenseTwoPlus,
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)':
                upt.licenses.GNUGeneralPublicLicenseThree,
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)': # noqa
                upt.licenses.GNUGeneralPublicLicenseThreePlus,
            'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)': # noqa
                upt.licenses.GNULesserGeneralPublicLicenseThreeDotZero,
            'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)': # noqa
                upt.licenses.GNULesserGeneralPublicLicenseThreeDotZeroPlus,
            'License :: OSI Approved :: IBM Public License':
                upt.licenses.IBMPublicLicense,
            'License :: OSI Approved :: Intel Open Source License':
                upt.licenses.IntelOpenSourceLicense,
            'License :: OSI Approved :: ISC License (ISCL)':
                upt.licenses.ISCLicense,
            # XXX: not available in upt
            # 'License :: OSI Approved :: Jabber Open Source License'
            'License :: OSI Approved :: MIT License':
                upt.licenses.MITLicense,
            # XXX: ot available in upt
            # 'License :: OSI Approved :: MITRE Collaborative Virtual Workspace License (CVW)' # noqa
            'License :: OSI Approved :: Motosoto License':
                upt.licenses.MotosotoLicense,
            'License :: OSI Approved :: Mozilla Public License 1.0 (MPL)':
                upt.licenses.MozillaPublicLicenseOneDotZero,
            'License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)':
                upt.licenses.MozillaPublicLicenseOneDotOne,
            'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)':
                upt.licenses.MozillaPublicLicenseTwoDotZero,
            'License :: OSI Approved :: Nethack General Public License':
                upt.licenses.NethackGeneralPublicLicense,
            'License :: OSI Approved :: Nokia Open Source License':
                upt.licenses.NokiaOpenSourceLicense,
            'License :: OSI Approved :: Open Group Test Suite License':
                upt.licenses.OpenGroupTestSuiteLicense,
            'License :: OSI Approved :: Python License (CNRI Python License)':
                upt.licenses.CNRIPythonLicense,
            'License :: OSI Approved :: Python Software Foundation License':
                upt.licenses.PythonLicenseTwoDotZero,
            'License :: OSI Approved :: Qt Public License (QPL)':
                upt.licenses.QPublicLicenseOneDotZero,
            'License :: OSI Approved :: Ricoh Source Code Public License':
                upt.licenses.RicohSourceCodePublicLicense,
            'License :: OSI Approved :: Sleepycat License':
                upt.licenses.SleepycatLicense,
            'License :: OSI Approved :: Sun Industry Standards Source License (SISSL)': # noqa
                upt.licenses.SunIndustryStandardsSourceLicenceOneDotOne,
            'License :: OSI Approved :: Sun Public License':
                upt.licenses.SunPublicLicense,
            'License :: OSI Approved :: Universal Permissive License (UPL)':
                upt.licenses.UniversalPermissiveLicense,
            'License :: OSI Approved :: University of Illinois/NCSA Open Source License': # noqa
                upt.licenses.NCSALicense,
            'License :: OSI Approved :: Vovida Software License 1.0':
                upt.licenses.VovidaSoftwareLicenseVOneDotZero,
            'License :: OSI Approved :: W3C License':
                upt.licenses.W3CLicense,
            'License :: OSI Approved :: X.Net License':
                upt.licenses.XNetLicense,
            'License :: OSI Approved :: zlib/libpng License':
                upt.licenses.ZlibLibpngLicense,
            'License :: OSI Approved :: Zope Public License':
                upt.licenses.ZopePublicLicenseTwoDotZero,
        }

        not_actual_licenses = [
            # These are licenses, but the version is not clearly specified.
            # NPL: 1.0 or 1.1?
            'License :: Netscape Public License (NPL)',
            # AFL: is it 1.1, 1.2, 2.0, 2.1 or 3.0?
            'License :: OSI Approved :: Academic Free License (AFL)',
            # ASL: is it 1.0, 1.1 or 2.0?
            'License :: OSI Approved :: Apache Software License',
            # APSL: is it 1.0, 1.1, 1.2 or 2.0?
            'License :: OSI Approved :: Apple Public Source License',
            # Artistic License: is it 1.0 or 2.0?
            'License :: OSI Approved :: Artistic License',
            # BSD: what version?
            'License :: OSI Approved :: BSD License',
            # FDL: what version?
            'License :: OSI Approved :: GNU Free Documentation License (FDL)',
            # GPL: what version?
            'License :: OSI Approved :: GNU General Public License (GPL)',
            # LGPLv2: v2.0 or v2.1?
            'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)', # noqa
            # LGPLv2+: v2.0+ or v2.1+?
            'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)', # noqa
            # 'LGPL' without a version: what version are we talking about?
            'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', # noqa
            # These are not actual licenses.
            'License :: DFSG approved',
            'License :: OSI Approved',
            'License :: Free For Educational Use',
            'License :: Free For Home Use',
            'License :: Free for non-commercial use',
            'License :: Freely Distributable',
            'License :: Free To Use But Restricted',
            'License :: Freeware',
            'License :: Other/Proprietary License',
            'License :: Public Domain',
            'License :: Repoze Public License',
        ]

        default = upt.licenses.UnknownLicense
        found = [all_license_classifiers.get(c, default)()
                 for c in self.classifiers
                 if c.startswith('License ::')
                 and c not in not_actual_licenses]

        # We found nothing: let's look at the sdist.
        # We found only one license, but could not identify it: same.
        # We found only one license, and could identify it: we're done.
        # We found more than one license: let's return everything. Even if some
        # of the found licenses are not properly identified, we're in a
        # "complex" case and it is probably best for a human to check what
        # licenses apply.
        if found and (len(found) > 1 or
                      not isinstance(found[0], default)):
            return found

        try:
            archive_url = self.get_sdist_archive_url(release)
            return self.guess_licenses_from_sdist(archive_url)
        except ValueError:
            return []

    def guess_licenses_from_sdist(self, archive_url):
        # TODO: we might want to use a wrapper around tarfile, zipfile and
        # other archive-related Python modules, rather than using this hack.
        if archive_url.endswith('.tar.gz'):
            open_archive = tarfile.open
            get_names = getattr(tarfile.TarFile, 'getnames')
        elif archive_url.endswith('.zip'):
            open_archive = zipfile.ZipFile
            get_names = getattr(zipfile.ZipFile, 'namelist')
        else:
            raise ValueError(f'Unknown sdist archive type at {archive_url}')

        licenses = []
        with tempfile.NamedTemporaryFile() as archive:
            urlretrieve(archive_url, archive.name)
            ar = open_archive(archive.name)
            license_files = [name for name in get_names(ar)
                             if name.endswith('/LICENSE')
                             or name.endswith('/LICENSE.txt')]
            if not license_files:
                return []

            with tempfile.TemporaryDirectory() as d:
                for license_file in license_files:
                    ar.extract(license_file, path=d)
                    path = f'{d}/{license_file}'
                    licenses.append(upt.licenses.guess_from_file(path))
        return licenses

    def get_archives(self, release):
        url, size, md5, sha256 = self.get_archive_info(release, 'sdist')
        archive = upt.Archive(url, size=size, md5=md5, sha256=sha256)
        return [archive]

    def parse(self, pkg_name):
        url = f'https://pypi.org/pypi/{pkg_name}/json'
        r = requests.get(url)
        if not r.ok:
            raise upt.InvalidPackageNameError(self.name, pkg_name)
        self.json = r.json()
        version = self.json['info']['version']
        self.classifiers = self.json['info'].get('classifiers', [])
        requirements = self.compute_requirements()
        d = {
            'homepage': self.json['info']['home_page'],
            'summary': self.json['info']['summary'],
            'description': self.json['info']['description'],
            'requirements': requirements,
            'licenses': self.guess_licenses(self.json['releases'][version]),
            'archives': self.get_archives(self.json['releases'][version]),
        }
        return PyPIPackage(pkg_name, version, **d)
