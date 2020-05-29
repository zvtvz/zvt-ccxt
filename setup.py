# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="zvt-ccxt",
    install_requires="zvt",
    entry_points={"zvt": ["ccxt = zvt_ccxt"]},
    py_modules=["zvt_ccxt"],
    packages=find_packages(),
    package_data={
        'zvt_ccxt.accounts': ['*.json']
    },
)
