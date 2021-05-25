# CurrencyConverter
## REST API для перевода валют

#### Сообщить нынешний курс: POST /database?merge=1 JSON: {"USD:RUR": 78.84, "EUR:RUR": 89.92}
merge = 0 - перед обновлением удалить данные
merge = 1 - объеденить данные, при конфликте заменить новыми

Ответ - JSON с нынешним состоянием состоянием курсов валют вида {"cr1:cr2": "ratio12", "cr3:cr4": "ratio34"}

### Перевести

GET /convert?from=RUR&to=USD&amount=42 - Перевести amount из валюты from в валюту to

Ответ - JSON {"from": "cr1", "to": "cr2", "amount_of_origin_currency": "amountcr1", "amount_of_target_currency": "amountcr2", "ERROR": "---"}

#### Перед запуском выполните "sudo apt-get install redis-server"

