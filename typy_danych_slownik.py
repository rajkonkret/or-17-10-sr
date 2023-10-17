# {"klucz" : "wartość"} - json
# słownik dane przechowywane w postaci klucz-wartość
# {'klucz' : 'warotść'}
slownik = {}  # pusty słownik
print(type(slownik))
print(slownik)  # {} - pusty słownik

slownik['imie'] = "Radek"
print(slownik)  # {'imie': 'Radek'}
slownik['wiek'] = 39
print(slownik)  # {'imie': 'Radek', 'wiek': 39}

print(slownik['imie'])  # Radek
# nazwa slownika, nawias [], nazwa klucza
slownik['imie'] = "Tomek"
print(slownik)  # {'imie': 'Tomek', 'wiek': 39}
print(type(slownik))  # <class 'dict'>
slownik.update({'imie': "Radek"})
print(slownik)  # {'imie': 'Raedek', 'wiek': 39}
slownik.update({"wzrost": 198})
print(slownik)  # {'imie': 'Raedek', 'wiek': 39, 'wzrost': 198}

print(slownik.keys())
print(slownik.values())
print(slownik.items())
# dict_keys(['imie', 'wiek', 'wzrost'])
# dict_values(['Radek', 39, 198])
# dict_items([('imie', 'Radek'), ('wiek', 39), ('wzrost', 198)])

slownik1 = {'a': 1, 'b': 2}
nowe_klucze = {'c': 3, 'd': 4, 'e': 5}
slownik1.update(nowe_klucze)
print(slownik1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

slownik2 = {'a': 1, 'b': 2}
slownik2 = {**slownik2, **nowe_klucze}
print(slownik2)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

slownik3 = {'x': 10, 'y': 20}
tuple_list = [("a", 1), ("b", 2), ("c", 3)]
slownik3.update(tuple_list)
print(slownik3)  # {'x': 10, 'y': 20, 'a': 1, 'b': 2, 'c': 3}

#
# print(slownik['z'])  # KeyError: 'z'
value = slownik3.get('z', 'Wartość domyślna')
print(value)  # Wartość domyślna
value = slownik3.get('a', 'Wartość domyślna')
print(value)  # 1
