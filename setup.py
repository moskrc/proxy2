# coding: utf-8

"""
Proxy2
-----
Author: https://github.com/inaz2
"""

import re
import ast
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('proxy2/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='Proxy2',
    version=version,
    url='https://github.com/inaz2/proxy2',
    license='BSD',
    author='inaz2',
    author_email='unknown@unknown.com',
    description='HTTP/HTTPS proxy in a single python script',
    packages=['proxy2', ],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points='''
        [console_scripts]
        proxy2_setup=proxy2:setup_https_intercept.sh
    '''
)