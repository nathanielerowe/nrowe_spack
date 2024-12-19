# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Larfinder(CMakePackage):
    """Common cmake bits for larsoft"""

    homepage = "https://github.com/LArSoft"
    url = "https://github.com/LArSoft/larfinder/archive/tags/v09_00_01.tar.gz"

    maintainers = ["marcmengel"]

    version("09_00_01", sha256="cfd2ce200a032e2e7cc7e8c510d2719965fb17e5571132e18be8574ad8a20144")
    version("develop", branch="develop", get_full_repo=True)

    depends_on("cetmodules", type="build")
