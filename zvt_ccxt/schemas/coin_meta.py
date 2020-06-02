# 数字货币
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract import EntityMixin
from zvt.contract.register import register_entity, register_schema

CoinMetaBase = declarative_base()


@register_entity(entity_type='coin')
class Coin(CoinMetaBase, EntityMixin):
    __tablename__ = 'coin'


register_schema(providers=['ccxt'], db_name='coin', schema_base=CoinMetaBase)

__all__ = ['Coin']
