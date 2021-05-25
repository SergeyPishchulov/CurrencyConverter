from money import Money, xrates
from decimal import Decimal


class Converter:
    def __init__(self, redis):
        self.exchange_rate = redis
        # exchange_rate[a:b]=v  --- a в v раз ценнее чем b

    def convert(self, cur_from, cur_to, amount):
        if cur_from == cur_to:
            return Money(amount, cur_from)
        if cur_from + ":" + cur_to in self.exchange_rate:
            ratio = self.exchange_rate[cur_from + ":" + cur_to].decode()
            xrates.base = cur_from
            xrates.setrate(cur_to, Decimal(ratio))
        elif cur_to + ":" + cur_from in self.exchange_rate:
            ratio = self.exchange_rate[cur_to + ":" + cur_from].decode()
            xrates.base = cur_to
            xrates.setrate(cur_from, Decimal(ratio))
        else:
            raise KeyError("No such exchange ratio")

        return Money(amount, cur_from).to(cur_to)

    def update_rate(self, updated, need_merge):
        if not need_merge:
            self.exchange_rate.flushall()
        for k in updated.keys():
            self.exchange_rate.set(k, updated[k])
