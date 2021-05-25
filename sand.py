import asyncio
import aioredis

import redis  # sudo apt-get install redis-server
from redis import Redis

r = redis.Redis(host='localhost', port=6379, db=0)
t = redis.Redis(host='localhost', port=6379, db=1)
t.flushall()
r.flushall()
t.set('1', 'one')
t.set('2', 'two')
r.set('3', 'three')
# print(r.set('foo', 'bar'))
for k in t.keys():
    r.set(k, t[k])
print(r['3'].decode())
print(r['1'].decode())
print(r.keys())

# print((t.mset(r)))
# print((t.update({'fr':'upd'})))
