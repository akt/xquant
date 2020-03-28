import hmac
import hashlib
import logging
import requests
import time

try:
    from urllib import urlencode

# for python3
except ImportError:
    from urllib.parse import urlencode

ENDPOINT = "https://www.binance.com"

BUY = "BUY"
SELL = "SELL"

LIMIT = "LIMIT"
MARKET = "MARKET"

GTC = "GTC"
IOC = "IOC"

options = {}


def time():
    data = request("GET", "/api/v3/time")
    return data["serverTime"]


def prices():
    """Get latest prices for all symbols."""
    data = request("GET", "/api/v1/ticker/allPrices")
    return {d["symbol"]: d["price"] for d in data}


def tickers():
    """Get best price/qty on the order book for all symbols."""
    data = request("GET", "/api/v1/ticker/allBookTickers")
    return {d["symbol"]: {
        "bid": d["bidPrice"],
        "ask": d["askPrice"],
        "bidQty": d["bidQty"],
        "askQty": d["askQty"],
    } for d in data}


def depth(symbol, **kwargs):
    """Get order book.
    Args:
        symbol (str)
        limit (int, optional): Default 100. Must be one of 50, 20, 100, 500, 5,
            200, 10.
    """
    params = {"symbol": symbol}
    params.update(kwargs)
    data = request("GET", "/api/v1/depth", params)
    return {
        "bids": {px: qty for px, qty in data["bids"]},
        "asks": {px: qty for px, qty in data["asks"]},
    }


def klines(symbol, interval, **kwargs):
    """Get kline/candlestick bars for a symbol.
    Klines are uniquely identified by their open time. If startTime and endTime
    are not sent, the most recent klines are returned.
    Args:
        symbol (str)
        interval (str)
        limit (int, optional): Default 500; max 500.
        startTime (int, optional)
        endTime (int, optional)
    """
    params = {"symbol": symbol, "interval": interval}
    params.update(kwargs)
    data = request("GET", "/api/v1/klines", params)
    return [{
        "openTime": d[0],
        "open": d[1],
        "high": d[2],
        "low": d[3],
        "close": d[4],
        "volume": d[5],
        "closeTime": d[6],
        "quoteVolume": d[7],
        "numTrades": d[8],
    } for d in data]


def request(method, path, params=None):
    resp = requests.request(method, ENDPOINT + path, params=params)
    data = resp.json()
    if "msg" in data:
        logging.error(data['msg'])
    return data


def formatNumber(x):
    if isinstance(x, float):
        return "{:.8f}".format(x)
    else:
        return str(x)
