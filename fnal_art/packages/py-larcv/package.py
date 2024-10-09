# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyLarcv(PythonPackage):
    """Framework for data processing to interface dnn open-source softwares"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://pypi.org/project/larcv"
    pypi = "larcv/larcv-3.5.1.tar.gz"

    version("3.5.1", sha256="7b3db26fc3fd0d640338896cc6ec1e0802bc042c0e7ad1ea07ff281b0f566ab3")

    depends_on("python")
    depends_on("py-numpy")
    depends_on("hdf5")
    depends_on("cmake", type="build")
    depends_on("py-scikit-build")

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args

