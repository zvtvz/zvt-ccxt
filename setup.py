# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt", session=False)

try:
    requirements = [str(ir.req) for ir in install_reqs]
except:
    requirements = [str(ir.requirement) for ir in install_reqs]

setup(
    name="zvt-ccxt",
    install_requires=requirements,
    entry_points={"zvt": ["ccxt = zvt_ccxt"]},
    py_modules=["zvt_ccxt"],
    packages=find_packages(),
    package_data={
        'zvt_ccxt.accounts': ['*.json']
    },
)
