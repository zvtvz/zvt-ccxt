# -*- coding: utf-8 -*-
from zvt.contract import IntervalLevel


def to_ccxt_trading_level(trading_level: IntervalLevel):
    return trading_level.value


from .coin_kdata_recorder import *
from .coin_tick_recorder import *
from .coin_recorder import *
