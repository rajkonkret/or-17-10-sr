class MyDict(dict):
    def __missing__(self, key):  # definiuje sposób obsłuzenia przypadku, gdy kluca nie ma w słowniku
        return "Nie ma takiego klucza"


class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key] = 0


class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            return self.get(key.lower())


d = MyDict()
d['name'] = 'Radek'
print(d['name'])
print(d['imie'])  # Nie ma takiego klucza

d2 = DefaultDict()
d2['name'] = 'Radek'
print(d2)
print(d2['imie'])  # default

d3 = AutoKeyDict()
d3['name'] = 'Radek'
print(d3['imie'])
print(d3)  # {'name': 'Radek', 'imie': 0}

d4 = CaseInsensitiveDict()
d4['name'] = 'Radek'
print(d4['Name'])