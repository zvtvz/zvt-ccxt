# -*- coding: utf-8 -*-

# ****** setting for crypto currency ****** #
COIN_EXCHANGES = ["binance", "huobipro"]

# COIN_BASE = ["BTC", "ETH", "XRP", "BCH", "EOS", "LTC", "XLM", "ADA", "IOTA", "TRX", "NEO", "DASH", "XMR",
#                        "BNB", "ETC", "QTUM", "ONT"]

COIN_BASE = ["BTC", "ETH", "EOS"]

COIN_PAIRS = [("{}/{}".format(item, "USDT")) for item in COIN_BASE] + \
             [("{}/{}".format(item, "USD")) for item in COIN_BASE]
