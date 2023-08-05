from collections import defaultdict

from .util import File

TEMPLATE = """\
# THIS FILE IS AUTOGENERATED DO NOT EDIT (IT WILL BE OVERWRITTEN).
[tox]
envlist = {env_matrix}

skipsdist = true

[testenv]
# Since tox doesnt install the package itself, it will not understand these commands without a whitelist.
whitelist_externals =
    scream
    flake8
    coverage
deps =
    scream

##############################
# Packages
##############################
{env_commands}
##############################
# Configuration
##############################

[flake8]
max-line-length = 120
ignore = E402

[coverage:run]
branch = True
omit =
    *tests/*
    *setup.py

[coverage:report]
exclude_lines =
    noqa
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:
omit =
    *__init__.py
    .tox/*

"""

TOX_COMMAND_TEMPL = """\
    {package_name}: flake8 {package_dir} --config={toxinidir}/tox.ini --statistics
    {package_name}: scream install {package_name}
    {package_name}: coverage run -a -m unittest discover -v -t {package_dir} -s {package_dir}/tests

"""


class Tox(File):
    def __init__(self, packages=None):

        if packages:

            env_matrix = []
            env_matrix_tmplate = "{{{pyversions}}}-{{{packages}}}"

            env_commands = "commands =\n"

            pyversion_matrix = defaultdict(list)

            for package in packages:
                env_commands += TOX_COMMAND_TEMPL.format(
                    package_name=package.package_name,
                    package_dir=package.package_dir,
                    toxinidir="{toxinidir}"
                )
                version_str = ','.join(package.tox_pyversions)

                pyversion_matrix[version_str].append(package.package_name)

            for pyversions, pkgs in pyversion_matrix.items():
                package_names = ','.join(pkgs)
                env_matrix.append(env_matrix_tmplate.format(pyversions=pyversions, packages=package_names))
            env_matrix_str = ','.join(env_matrix)

        # This is probably a new repo...
        else:
            env_commands = 'commands = flake8 .'
            env_matrix_str = 'py37'

        super(Tox, self).__init__(
            'tox.ini',
            TEMPLATE.format(
                env_commands=env_commands,
                env_matrix=env_matrix_str
            )
        )
