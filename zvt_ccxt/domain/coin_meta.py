# 数字货币
import pandas as pd
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract import EntityMixin
from zvt.contract.register import register_entity, register_schema

CoinMetaBase = declarative_base()


@register_entity(entity_type='coin')
class Coin(CoinMetaBase, EntityMixin):
    __tablename__ = 'coin'

    @classmethod
    def get_trading_dates(cls, start_date=None, end_date=None):
        return pd.date_range(start_date, end_date, freq='D')

    @classmethod
    def could_short(cls):
        return True

    @classmethod
    def get_trading_t(cls):
        return 0

    @classmethod
    def get_trading_intervals(cls):
        return [('00:00,23:59')]


register_schema(providers=['ccxt'], db_name='coin', schema_base=CoinMetaBase)

__all__ = ['Coin']
