from zvt.schemas import KdataCommon, TickCommon


class CoinKdataCommon(KdataCommon):
    pass


class CoinTickCommon(TickCommon):
    pass


from .coin_meta import *
from .quotes import *
