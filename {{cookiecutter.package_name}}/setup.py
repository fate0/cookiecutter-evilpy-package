#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import sys
import json
import setuptools
from setuptools.command.install import install


class AbortInstall(install):
    def run(self):
        raise SystemExit(
            "[+] It looks like you try to install {{ cookiecutter.package_name }} without checking it.\n"
            "[-] is that alright? \n"
            "[*] Please visit http://evilpackage.fatezero.org/ \n"
            "[/] Aborting installation."
        )


setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}",
    url="http://evilpackage.fatezero.org/",

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",

    description="{{ cookiecutter.package_desc }}",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),
    cmdclass={
        'install': AbortInstall
    },

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)


