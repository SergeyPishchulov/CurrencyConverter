import json
from money import Money, xrates
from decimal import Decimal
from converter import Converter
from aiohttp import web
import redis

xrates.install('money.exchange.SimpleBackend')
xrates.base = 'USD'
r = redis.Redis(host='localhost', port=6379, db=0)
r.flushall()
converter = Converter(r)


async def update_exchange_rate(request):
    params = request.rel_url.query
    merge_flag = int(params['merge'])
    new_rate = await request.json()
    converter.update_rate(new_rate, merge_flag)
    return web.Response(text=json.dumps(
        {k.decode(): converter.exchange_rate[k].decode()
         for k in converter.exchange_rate.keys()}))


async def convert(request):
    params = request.rel_url.query
    currency_from = params['from']
    currency_to = params['to']
    amount = Decimal(params['amount'])

    try:
        converted = converter.convert(currency_from, currency_to, amount)
    except KeyError as e:
        return web.Response(text=json.dumps({"from": currency_from,
                                             "to": currency_to,
                                             "amount_of_origin_currency": str(amount),
                                             "amount_of_target_currency": "---",
                                             "ERROR": str(e)
                                             }))
    return web.Response(text=json.dumps({"from": currency_from,
                                         "to": currency_to,
                                         "amount_of_origin_currency": str(amount),
                                         "amount_of_target_currency": str(converted.amount),
                                         "ERROR": "---"
                                         }))


app = web.Application()
app.add_routes([
    web.get('/convert', convert),
    web.post('/database', update_exchange_rate)
])

if __name__ == '__main__':
    web.run_app(app)
