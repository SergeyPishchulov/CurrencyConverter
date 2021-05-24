import requests

resp = requests.post("http://localhost:8080/database?merge=1",
                     json={
                         "USD:RUR": 60,
                         "EUR:RUR": 1.2,
                         "CAD:USD": 1.1,
                         "CAD:RUR": 55,
                         "EUR:CAD": 1.4
                     })

print(resp.text)


resp=requests.get("http://localhost:8080/convert?from=EUR&to=RUR&amount=120", '')
print(resp.text)
