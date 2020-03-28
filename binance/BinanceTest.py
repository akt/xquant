import BinanceMethod as bm
import BinanceOpenMethod as bom


SYMBOL = "BTCUSDT"
# print(bm.prices())

# print(bm.tickers())

# print(bm.time())
# print(bm.balances())
# print(bm.depth(SYMBOL))
print(bom.klines(SYMBOL, "1w"))
