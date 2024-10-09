# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Htgettoken(Package):
    """Utility to fetch webtokens from Vault"""

    homepage = "https://github.com/fermitools/htgettoken"
    url = "https://github.com/fermitools/htgettoken/archive/refs/tags/v1.15.tar.gz"

    maintainers = ["marcmengel", "DrDaveD"]

    version(
        "1.15",
        sha256="87e2e72d6d79cf8df7d7b1fcf4d4570acf6e6d85566b7d2817bd777cbb82d653",
    )
    version(
        "1.14",
        sha256="69b9f725ea63231d05fb53757f18c8bbf0192419d196953f684a5f297e19aeeb",
    )

    depends_on("py-m2crypto", type=("build", "run"))
    depends_on("py-pyopenssl", type=("build", "run"))
    depends_on("py-kerberos", type=("build", "run"))
    depends_on("coreutils", type="run")  # for 'base64'

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        mkdir(prefix.man)
        filter_file("#!/usr/bin/python3", "#!/usr/bin/env python3", "htgettoken")
        install("htgettoken", prefix.bin)
        install("httokendecode", prefix.bin)
        install("htgettoken.1", prefix.man)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
