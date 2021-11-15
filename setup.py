#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sphinx directive for "sessions", like typing into a console or Python prompt.
"""

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = (
    open(os.path.join(here, 'README.rst')).read()
)

install_requires = [
    'Sphinx',
    'pygments',
]
setup_requires = [
]
tests_require = [
]

setup(
    name='sphinxcontrib-session',
    version='0.0.1',
    description=__doc__.strip(),
    long_description=README,
    long_description_content_type='text/x-rst',
    classifiers=[
        'Development Status :: 3 - Alpha'
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2.0',
        'Programming Language :: Python',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    author="Tim 'mithro' Ansell",
    author_email='me@mith.ro',
    url='http://github.com/mithro/sphinxcontrib-session',
    license='Apache 2.0',
    keywords='sphinx pygments shell-session ps1con console doscon',
    packages=find_packages(exclude=["*.tests", "*.tests.*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
)
