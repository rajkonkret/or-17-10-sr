# json - klucz-wartosc
# {"name" : "radek"}
import json

print(json)
# <module 'json' from 'C:\\Users\\CSComarch\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\json\\__init__.py'>

json_string = '{"name":"Jan", "age" :30, "city":"Lodz"}'
data = json.loads(json_string)  # zamiana na słownik
print(data)  # {'name': 'Jan', 'age': 30, 'city': 'Lodz'}
print(type(json_string))  # <class 'str'>
print(type(data))  # <class 'dict'>

data2 = {
    "name": "Jan",
    "age": 30,
    "city": "Łódź",
}

json_string2 = json.dumps(data2)  # zamiana jsona
print(json_string2)  # {"name": "Jan", "age": 30, "city": "Lodz"}
print(type(json_string2))

data = json.loads(json_string2)
print(data['name'])
print(data['age'])
print(data['city'])

data['country'] = "Polska"
del data['city']
print(data)
data['car'] = [{"color": "blue"}, {"brand": "Fiat"}]
modifed_json = json.dumps(data)
print(modifed_json)
# {'name': 'Jan', 'age': 30, 'country': 'Polska'}
# {"name": "Jan", "age": 30, "country": "Polska"}
# {"name": "Jan", "age": 30, "country": "Polska", "car": [{"color": "blue"}, {"brand": "Fiat"}]}

person_dict = {'name': 'Radek', 'city': "Łódź", 'age': "38", "czy_pali": None}
with open('dane.json', 'w', encoding='utf-8') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)

with open('dane.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data)
print(type(data))  # <class 'dict'>
# 13:20
