# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install larcv2
#
# You can edit this file again by typing:
#
#     spack edit larcv2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
from spack.util.environment import EnvironmentModifications
import os
import platform

class Larcv2(MakefilePackage):
    """Framework for data processing with APIs to interface deep neural network"""

    homepage = "https://github.com/DeepLearnPhysics/larcv2"
    url = "https://github.com/DeepLearnPhysics/larcv2/archive/refs/tags/v2_2_6.tar.gz"

    version("2_2_6", sha256="2d301967017e14453110122a3b2abb0070ab57e9c2b5b6e9cc8b6aaa8f0b656b")
    version("2_2_5", sha256="0536d09018cada91dcdd0b0c5d365c6cecb8b1790ed7359d2a90d23446bf51c7")
    version("2_2_1", sha256="e104579f7e2ffa8564a1c8c73947f3416099528e04eede204d40c8b8c118fa88")
    version("2_2_0", sha256="b70ebe95bea2b37644c45d48a8a402d3bdc83c44b743b69745ce9f29183a6e73")

    depends_on("root", type=("build", "run"))

    phases = ['build', 'install']

    def setup_build_environment(self, env):
        self.stage.create()
        self.stage.fetch()
        self.stage.expand_archive()
        env.extend(EnvironmentModifications.from_sourcing_file(self.stage.source_path+"/configure.sh"))

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        install_tree(self.stage.source_path+"/build", prefix)
        install_tree(self.stage.source_path+"/python", prefix+"/python")# Either this or PYTHONPATH line fixed an issue

    def setup_run_environment(self, run_env):
        run_env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        run_env.prepend_path("LARCV2_LIBDIR", self.prefix.lib)
        run_env.prepend_path("LARCV2_LIB", self.prefix.lib)
        run_env.prepend_path("LARCV2_INCDIR", self.prefix.include)
        run_env.prepend_path("LARCV2_INC", self.prefix.include)
        run_env.prepend_path("PYTHONPATH", self.prefix.include.python)
