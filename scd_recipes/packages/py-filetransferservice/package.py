# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.package import *


class PyFiletransferservice(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "http://cdcvs.fnal.gov/redmine/projects/filetransferservice"
    url = "http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/filetransferservice.v6_3_5.tar"

    version(
        "6_3_5",
        sha256="3ca8b2507d56b2a836cd8141c200a4618f9e22fd54d5478e69208bbfd0d21643",
    )

    depends_on("py-setuptools", type="build")
    depends_on("py-twisted", type=("build", "run"))
    depends_on("py-service-identity", type=("build", "run"))
    depends_on("py-pyopenssl", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-crcmod", type=("build", "run"))
    depends_on("py-sam-cp", type="run")
    depends_on("ifdhc cxxstd=default", type="run")
