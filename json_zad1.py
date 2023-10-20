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
    "city": "Łódź"
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

modifed_json = json.dumps(data)
print(modifed_json)
# {'name': 'Jan', 'age': 30, 'country': 'Polska'}
# {"name": "Jan", "age": 30, "country": "Polska"}
