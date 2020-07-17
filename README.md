[![github](https://img.shields.io/github/stars/zvtvz/zvt-ccxt.svg)](https://github.com/zvtvz/zvt-ccxt)
[![image](https://img.shields.io/pypi/v/zvt-ccxt.svg)](https://pypi.org/project/zvt-ccxt/)
[![image](https://img.shields.io/pypi/l/zvt-ccxt.svg)](https://pypi.org/project/zvt-ccxt/)
[![image](https://img.shields.io/pypi/pyversions/zvt-ccxt.svg)](https://pypi.org/project/zvt-ccxt/)
[![Build Status](https://api.travis-ci.org/zvtvz/zvt-ccxt.svg?branch=master)](https://travis-ci.org/zvtvz/zvt-ccxt)
[![HitCount](http://hits.dwyl.io/zvtvz/zvt-ccxt.svg)](http://hits.dwyl.io/zvtvz/zvt-ccxt)

##  How to use
### 1.1 install
```
pip install zvt-ccxt

pip show zvt-ccxt
```

make sure use the latest version
```
pip install --upgrade zvt-ccxt
```

###  1.2 use in zvt way
```
In [1]: from zvt_ccxt.domain import *

In [2]: Coin
Out[2]: zvt_ccxt.domain.coin_meta.Coin

In [3]: Coin.record_data()
Coin registered recorders:{'ccxt': <class 'zvt_ccxt.recorders.coin_recorder.CoinMetaRecorder'>}

2020-07-17 23:26:38,730  INFO  MainThread  init_markets for binance success
2020-07-17 23:26:40,941  INFO  MainThread  init_markets for huobipro success
In [4]: Coin.query_data()
Out[4]:
                       id               entity_id timestamp entity_type  exchange      code      name
0   coin_binance_BTC/USDT   coin_binance_BTC/USDT      None        coin   binance  BTC/USDT  BTC/USDT
1   coin_binance_ETH/USDT   coin_binance_ETH/USDT      None        coin   binance  ETH/USDT  ETH/USDT
2   coin_binance_EOS/USDT   coin_binance_EOS/USDT      None        coin   binance  EOS/USDT  EOS/USDT
3  coin_huobipro_BTC/USDT  coin_huobipro_BTC/USDT      None        coin  huobipro  BTC/USDT  BTC/USDT
4  coin_huobipro_ETH/USDT  coin_huobipro_ETH/USDT      None        coin  huobipro  ETH/USDT  ETH/USDT
5  coin_huobipro_EOS/USDT  coin_huobipro_EOS/USDT      None        coin  huobipro  EOS/USDT  EOS/USDT


In [2]: Coin1dKdata.record_data()
In [4]: Coin1dKdata.query_data(codes=['BTC/USDT'])
Out[4]:
                                   id              entity_id  timestamp provider      code      name level     open    close     high      low        volume turnover
0    coin_binance_BTC/USDT_2017-10-22  coin_binance_BTC/USDT 2017-10-22     ccxt  BTC/USDT  BTC/USDT    1d  6003.27  5950.02  6060.00  5720.03   1362.092216     None
1    coin_binance_BTC/USDT_2017-10-23  coin_binance_BTC/USDT 2017-10-23     ccxt  BTC/USDT  BTC/USDT    1d  5975.00  5915.93  6080.00  5621.03   1812.557715     None
2    coin_binance_BTC/USDT_2017-10-24  coin_binance_BTC/USDT 2017-10-24     ccxt  BTC/USDT  BTC/USDT    1d  5909.47  5477.03  5925.00  5450.00   2580.418767     None
3    coin_binance_BTC/USDT_2017-10-25  coin_binance_BTC/USDT 2017-10-25     ccxt  BTC/USDT  BTC/USDT    1d  5506.92  5689.99  5704.96  5286.98   2282.813205     None
4    coin_binance_BTC/USDT_2017-10-26  coin_binance_BTC/USDT 2017-10-26     ccxt  BTC/USDT  BTC/USDT    1d  5670.10  5861.77  5939.99  5650.00   1972.965882     None
..                                ...                    ...        ...      ...       ...       ...   ...      ...      ...      ...      ...           ...      ...
995  coin_binance_BTC/USDT_2020-07-13  coin_binance_BTC/USDT 2020-07-13     ccxt  BTC/USDT  BTC/USDT    1d  9303.31  9242.62  9343.82  9200.89  42740.069115     None
996  coin_binance_BTC/USDT_2020-07-14  coin_binance_BTC/USDT 2020-07-14     ccxt  BTC/USDT  BTC/USDT    1d  9242.61  9255.85  9279.54  9113.00  45772.552509     None
997  coin_binance_BTC/USDT_2020-07-15  coin_binance_BTC/USDT 2020-07-15     ccxt  BTC/USDT  BTC/USDT    1d  9255.85  9197.60  9276.49  9160.57  39053.579665     None
998  coin_binance_BTC/USDT_2020-07-16  coin_binance_BTC/USDT 2020-07-16     ccxt  BTC/USDT  BTC/USDT    1d  9197.60  9133.72  9226.15  9047.25  43375.571191     None
999  coin_binance_BTC/USDT_2020-07-17  coin_binance_BTC/USDT 2020-07-17     ccxt  BTC/USDT  BTC/USDT    1d  9133.72  9157.72  9186.83  9089.81  21075.560207     None

[1000 rows x 13 columns]
```


## 💌请作者喝杯咖啡

如果你觉得项目对你有帮助,可以请作者喝杯咖啡  
<img src="https://raw.githubusercontent.com/zvtvz/zvt/master/docs/imgs/alipay-cn.png" width="25%" alt="Alipay">　　　　　
<img src="https://raw.githubusercontent.com/zvtvz/zvt/master/docs/imgs/wechat-cn.png" width="25%" alt="Wechat">

## 🤝联系方式  

个人微信:foolcage 添加暗号:zvt-ccxt  
<img src="https://raw.githubusercontent.com/zvtvz/zvt/master/docs/imgs/wechat.jpeg" width="25%" alt="Wechat">

------
微信公众号:  
<img src="https://raw.githubusercontent.com/zvtvz/zvt/master/docs/imgs/gongzhonghao.jpg" width="25%" alt="Wechat">

知乎专栏:  
https://zhuanlan.zhihu.com/automoney

## Thanks
<p><a href=https://www.jetbrains.com/?from=zvt><img src="https://raw.githubusercontent.com/zvtvz/zvt/master/docs/imgs/jetbrains.png" width="25%" alt="jetbrains"></a></p>