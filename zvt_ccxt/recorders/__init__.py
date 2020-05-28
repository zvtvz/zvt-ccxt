# -*- coding: utf-8 -*-
from zvt.core import IntervalLevel


def to_ccxt_trading_level(trading_level: IntervalLevel):
    return trading_level.value