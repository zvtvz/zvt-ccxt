# -*- coding: utf-8 -*-
import zvt
from zvt_ccxt.accounts import CCXTAccount


@zvt.hookimpl
def zvt_setup_env(config: dict):
    return "zvt_ccxt", CCXTAccount.exchange_conf


from zvt_ccxt.domain import *
from zvt_ccxt.recorders import *
