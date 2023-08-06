# Vexbi Python Library

[![Coverage Status][coveralls-image]][coveralls-url]
[![Build Status][travis-image]][travis-url]
[![PyPI version][pypi-image]][pypi-url]

Python library for [Vexbi](https://www.vexbi.com/) API. Please read our [documentation](#) for instructions on how to start using the API.

## Requirements

- Python 2.7.0+
- Git 1.7.0+

## Getting started

### install dependencies:

```
pip install -r requirements.txt
```

## Usage

### #create_order
### /v2/orders
##### ***POST***

**Summary:** Create a Sell/Buy order.
**Description:** Create a Sell/Buy order.

**Parameters**


| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| market | formData | Unique market id. It's always in the form of xxxyyy, where xxx is the base currency code, yyy is the quote currency code, e.g. 'btcusd'. All available markets can be found at /api/v2/markets. | Yes | string |
| side | formData | Either 'sell' or 'buy'. | Yes | string |
| volume | formData | The amount user want to sell/buy. An order could be partially executed, e.g. an order sell 5 btc can be matched with a buy 3 btc order, left 2 btc to be sold; in this case the order's volume would be '5.0', its remaining_volume would be '2.0', its executed volume is '3.0'. | Yes | string |
| price | formData | Price for each unit. e.g. If you want to sell/buy 1 btc at 3000 usd, the price is '3000.0' | No | string |
| ord_type | formData | The type of order, can be `market` or `limit`  | No (defaults to `limit` | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 | Create a Sell/Buy order. |

### #delete_order
### /v2/order/delete
##### ***POST***

**Summary:** Cancel an order.
**Description:** Cancel an order.

**Parameters**

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | formData | Unique order id. | Yes | integer |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 | Cancel an order. |

### #clear_all
### /v2/orders/clear
##### ***POST***

**Summary:** Cancel all my orders.
**Description:** Cancel all my orders.

**Parameters**

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| side | formData | If present, only sell orders (asks) or buy orders (bids) will be canncelled. | No | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 | Cancel all my orders. |

### #get_orders
### /v2/orders
##### ***GET***

**Summary:** Get your orders, results is paginated.
**Description:** Get your orders, results is paginated.

**Parameters**

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| market | query | Unique market id. It's always in the form of xxxyyy, where xxx is the base currency code, yyy is the quote currency code, e.g. 'btcusd'. All available markets can be found at /api/v2/markets. | Yes | string |
| state | query | Filter order by state, default to 'wait' (active orders). | No | string |
| limit | query | Limit the number of returned orders, default to 100. | No | integer |
| page | query | Specify the page of paginated results. | No | integer |
| order_by | query | If set, returned orders will be sorted in specific order, default to 'asc'. | No | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 | Get your orders, results is paginated. |

### #get_order
### /v2/order
##### ***GET***

**Summary:** Get information of specified order.
**Description:** Get information of specified order.

**Parameters**

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | query | Unique order id. | Yes | integer |

### #get_account_info
### /v2/members/me
##### ***GET***

**Summary:** Get your profile and accounts info.
**Description:** Get your profile and accounts info.

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 | Get your profile and accounts info. |

### #get_available_markets
### /v2/markets
##### ***GET***

**Summary:** Get all available markets.

**Description:** Get all available markets.

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 | Get all available markets. |

### #tickers
### /v2/tickers
##### ***GET***

**Summary:** Get ticker of all markets.
**Description:** Get ticker of all markets.

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 | Get ticker of all markets. |

### #trades
### /v2/trades
##### ***GET***

**Summary:** Get recent trades on market, each trade is included only once. Trades are sorted in reverse creation order.
**Description:** Get recent trades on market, each trade is included only once. Trades are sorted in reverse creation order.

**Parameters**

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| market | query | Unique market id. It's always in the form of xxxyyy, where xxx is the base currency code, yyy is the quote currency code, e.g. 'btcusd'. All available markets can be found at /api/v2/markets. | Yes | string |
| limit | query | Limit the number of returned trades. Default to 50. | No | integer |
| timestamp | query | An integer represents the seconds elapsed since Unix epoch. If set, only trades executed before the time will be returned. | No | integer |
| from | query | Trade id. If set, only trades created after the trade will be returned. | No | integer |
| to | query | Trade id. If set, only trades created before the trade will be returned. | No | integer |
| order_by | query | If set, returned trades will be sorted in specific order, default to 'desc'. | No | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 | Get recent trades on market, each trade is included only once. Trades are sorted in reverse creation order. |

### #my_trades
### /v2/trades/my
##### ***GET***

**Summary:** Get your executed trades. Trades are sorted in reverse creation order.
**Description:** Get your executed trades. Trades are sorted in reverse creation order.

**Parameters**

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| market | query | Unique market id. It's always in the form of xxxyyy, where xxx is the base currency code, yyy is the quote currency code, e.g. 'btcusd'. All available markets can be found at /api/v2/markets. | Yes | string |
| limit | query | Limit the number of returned trades. Default to 50. | No | integer |
| timestamp | query | An integer represents the seconds elapsed since Unix epoch. If set, only trades executed before the time will be returned. | No | integer |
| from | query | Trade id. If set, only trades created after the trade will be returned. | No | integer |
| to | query | Trade id. If set, only trades created before the trade will be returned. | No | integer |
| order_by | query | If set, returned trades will be sorted in specific order, default to 'desc'. | No | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 | Get your executed trades. Trades are sorted in reverse creation order. |

## Test

Just clone the repo, install dependencies as you would in development and run `nose2` or `python setup.py test`

## Contributing

1. Fork it ( https://github.com/vexbiexchange/python-api-client/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

[coveralls-image]: https://coveralls.io/repos/github/vexbiexchange/python-api-client/badge.svg?branch=master
[coveralls-url]: https://coveralls.io/github/vexbiexchange/python-api-client?branch=master

[travis-image]: https://travis-ci.org/vexbiexchange/python-api-client.svg?branch=master
[travis-url]: https://travis-ci.org/vexbiexchange/python-api-client

[pypi-image]: https://badge.fury.io/py/vexbi.svg
[pypi-url]: https://badge.fury.io/py/vexbi
