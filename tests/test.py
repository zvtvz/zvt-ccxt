# -*- coding: utf-8 -*-
from zvt_ccxt.domain import Coin


def test_coin():
    try:
        Coin.record_data()
        Coin.query_data()
    except:
        assert False
