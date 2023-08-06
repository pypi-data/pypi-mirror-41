##
# Copyright 2018-2019 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://www.vscentrum.be),
# Flemish Research Foundation (FWO) (http://www.fwo.be/en)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# https://github.com/easybuilders/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
EasyBuild support for installing a software-specific .modulerc file

@author: Kenneth Hoste (Ghent University)
"""
import os

from easybuild.framework.easyblock import EasyBlock
from easybuild.tools.build_log import EasyBuildError, print_msg
from easybuild.tools.filetools import mkdir, symlink


class ModuleRC(EasyBlock):
    """
    Generic easyblock to create a software-specific .modulerc file
    """

    def configure_step(self):
        """Do nothing."""
        pass

    def build_step(self):
        """Do nothing."""
        pass

    def install_step(self):
        """Do nothing."""
        pass

    def make_module_step(self, fake=False):
        """Install .modulerc file."""
        modfile_path = self.module_generator.get_module_filepath(fake=fake)
        modulerc = os.path.join(os.path.dirname(modfile_path), self.module_generator.DOT_MODULERC)

        deps = self.cfg['dependencies']
        if len(deps) != 1:
            raise EasyBuildError("There should be exactly one dependency specified, found %d", len(deps))

        # names should match
        if self.name != deps[0]['name']:
            raise EasyBuildError("Name does not match dependency name: %s vs %s", self.name, deps[0]['name'])

        # ensure version to alias to is a prefix of the version of the dependency
        if not deps[0]['version'].startswith(self.version):
            raise EasyBuildError("Version is not a prefix of dependency version: %s vs %s",
                                 self.version, deps[0]['version'])

        alias_modname = deps[0]['short_mod_name']
        self.log.info("Adding module version alias for %s to %s", alias_modname, modulerc)

        # add symlink to wrapped module file when generating .modulerc in temporary directory (done during sanity check)
        # this is strictly required for Lmod 6.x, for which .modulerc and wrapped module file must be in same location
        if fake:
            wrapped_mod_path = self.modules_tool.modulefile_path(alias_modname)
            wrapped_mod_filename = os.path.basename(wrapped_mod_path)
            target = os.path.join(os.path.dirname(modulerc), wrapped_mod_filename)
            mkdir(os.path.dirname(target), parents=True)
            symlink(wrapped_mod_path, target)

        module_version_specs = {
            'modname': alias_modname,
            'sym_version': self.version,
            'version': deps[0]['version'],
        }
        self.module_generator.modulerc(module_version=module_version_specs, filepath=modulerc)

        if not fake:
            print_msg("created .modulerc file at %s" % modulerc, log=self.log)

        modpath = self.module_generator.get_modules_path(fake=fake)
        self.invalidate_module_caches(modpath)

        return modpath

    def sanity_check_step(self, *args, **kwargs):
        """
        Custom sanity check: just try to load the module version alias
        """
        # test loading of (fake) module by means of sanity check
        fake_mod_data = self.load_fake_module(purge=True)
        self.clean_up_fake_module(fake_mod_data)
