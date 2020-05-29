# 数字货币
from sqlalchemy.ext.declarative import declarative_base

from zvt.core import EntityMixin
from zvt.core.contract import register_entity, register_schema

CoinMetaBase = declarative_base()


@register_entity(entity_type='coin')
class Coin(CoinMetaBase, EntityMixin):
    __tablename__ = 'coin'


register_schema(providers=['ccxt'], db_name='coin', schema_base=CoinMetaBase)

__all__ = ['Coin']
