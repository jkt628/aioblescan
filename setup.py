#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from distutils.core import setup

setup(name='aioblescan',
    packages=['aioblescan'],
    version='0.1.0',
    author='François Wautier',
    author_email='francois@wautier.eu',
    description='Scanning Bluetooth for advertised info with asyncio.',
    url='http://github.com/frawau/aioblescan',
    download_url='https://github.com/frawau/aioblescan/archive/0.1.0.tar.gz',  
    keywords = ['bluetooth', 'advertising', 'hci'], 
    license='MIT',
    install_requires=[],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ])
