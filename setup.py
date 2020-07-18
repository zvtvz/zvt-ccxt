# -*- coding: utf-8 -*-
# To use a consistent encoding
from codecs import open
from os import path

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

install_reqs = parse_requirements("requirements.txt", session=False)

try:
    requirements = [str(ir.req) for ir in install_reqs]
except:
    requirements = [str(ir.requirement) for ir in install_reqs]

setup(
    name="zvt-ccxt",
    version='0.0.6',
    description='ccxt cryptocurrency plugin for zvt ',
    install_requires=requirements,
    entry_points={"zvt": ["ccxt = zvt_ccxt"]},
    py_modules=["zvt_ccxt"],
    packages=find_packages(),
    package_data={
        'zvt_ccxt.accounts': ['*.json']
    },
    long_description=long_description,
    url='https://github.com/zvtvz/zvt-ccxt',
    author='foolcage',
    author_email='5533061@qq.com',
    classifiers=[  # Optional
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Office/Business :: Financial :: Investment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    keywords='quant zvt cryptocurrency coin btc eos',

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/zvtvz/zvt-ccxt/issues',
        'Funding': 'https://github.com/zvtvz/zvt-ccxt',
        'Say Thanks!': 'https://saythanks.io/to/foolcage',
        'Source': 'https://github.com/zvtvz/zvt-ccxt',
    },

    include_package_data=True,
    long_description_content_type="text/markdown",
)
