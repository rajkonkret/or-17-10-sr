import json
import requests as re
from pydantic import BaseModel

# pip install requests

url = "http://api.nbp.pl/api/exchangerates/rates/A/EUR"
# REST API
# get, post, put, patch, delete, head, option
# create, read, update, delete - CRUD
# json
response = re.get(url)
print(response)  # <Response [200]>
# 404 - błedny adres
# 400 - błedne zapytanie
# W przypadku braku danych dla prawidłowo określonego zakresu czasowego zwracany jest komunikat 404 Not Found
# W przypadku zadania nieprawidłowo sformułowanych zapytań serwis zwraca komunikat 400 Bad Request
# W przypadku zapytania przekraczającego limit zwracanych danych serwis zwróci komunikat
# 400 Bad Request - Przekroczony limit

dane = response.json()
# print(dane)
print(type(dane))  # <class 'list'>
print(dane)  # {'table': 'A', 'currency': 'euro', 'code': 'EUR',


# 'rates': [{'no': '204/A/NBP/2023', 'effectiveDate': '2023-10-20', 'mid': 4.4675}]}


class Rate(BaseModel):
    no: str
    effectiveDate: str
    mid: float


class CurrencyData(BaseModel):
    table: str
    currency: str
    code: str
    rates: list[Rate]


json_string = json.dumps(dane)
# currency_data = CurrencyData.parse_raw(json_string)
currency_data2 = CurrencyData.model_validate_json(json_string)
# print(currency_data)
# table='A' currency='euro' code='EUR' rates=[Rate(no='204/A/NBP/2023', effectiveDate='2023-10-20', mid=4.4675)]
# print(currency_data.code)  # EUR
# print(currency_data.rates[0].effectiveDate)  # 2023-10-20
print(currency_data2)
# C:\Users\CSComarch\PycharmProjects\or-17-10-sr\json_zad2.py:44: PydanticDeprecatedSince20: The `parse_raw` method is deprecated; if your data is JSON use `model_validate_json`, otherwise load the data then use `model_validate` instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.4/migration/
#   currency_data = CurrencyData.parse_raw(json_string)
# 14:10
