from zvt.contract import IntervalLevel
from zvt.domain.quotes.gen_kdata_schema import gen_kdata_schema

if __name__ == '__main__':
    gen_kdata_schema(pkg='zvt_ccxt', providers=['ccxt'], entity_type='coin',
                     levels=[level for level in IntervalLevel])
