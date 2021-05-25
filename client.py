import requests
import unittest

eur_rur = 89.92
resp = requests.post("http://localhost:8080/database?merge=1",
                     json={
                         "USD:RUR": 60,
                         "EUR:RUR": eur_rur,
                         "CAD:USD": 1.1,
                         "CAD:RUR": 55,
                         "EUR:CAD": 1.4
                     })
print(resp.text)
resp = requests.get("http://localhost:8080/convert?from=EUR&to=RUR&amount=1", '')
print(resp.text)

resp = requests.post("http://localhost:8080/database?merge=0",
                     json={
                         "USD:RUR": 60
                     })
print(resp.text)

resp = requests.get("http://localhost:8080/convert?from=USD&to=RUR&amount=120", '')
print(resp.text)

resp = requests.get("http://localhost:8080/convert?from=NON&to=RUR&amount=120", '')
print(resp.text)
