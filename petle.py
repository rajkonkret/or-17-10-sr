# # for - petla iteracyjna
from itertools import zip_longest

#
# lista = []
#
# for i in range(6):  # 0..5
#     print(i)
#     if i % 2 == 0:
#         print("Jest parzysta", i, end='', sep=";")
#         lista.append(i)
#
# print(lista)  # [0, 2, 4]
# lista2 = [j for j in range(6) if j % 2 == 0]  # [j] - odpowiednik append
# print(lista2)
# lista3 = [j if j % 2 == 0 else 10 for j in range(6)]
# print(lista3)  # [0, 10, 2, 10, 4, 10]
#
# for c in lista2:
#     if c == 2:
#         c += 1  # c = c + 1
#     print(c)  # 3
#
# # +=, -=, *=, /=, %=
# a = 1
# a += 1  # a = a + 1
# print(a)
# a -= 3  # a = a - 3
# print(a)
# a *= 2  # a = a * 2
# print(a)
# a /= 2  # a = a / 2
# print(a)  # -1.0
# # dzielenie daje wynik float
# a %= 2
# print(a)  # 1.0
#
# imiona = ["Radek", "Zenek", "Monika"]
# print(imiona)  # ['Radek', 'Zenek', 'Monika']
# print(type(imiona))  # <class 'list'>
#
# for p in imiona:
#     print(p)
# # Radek
# # Zenek
# # Monika
# # wypisaniu tego ale razem z indeksem
# # enumerte()
# for p in enumerate(imiona):
#     print(p)  # (1, 'Zenek')
#
# for pozycja, osoba in enumerate(imiona, start=1):
#     print(pozycja, osoba)  # 1 Zenek
# # 1 Radek
# # 2 Zenek
# # 3 Monika
# print(imiona.index("Radek"))  # 0

ludzie = ['Radek', 'Janek', 'Asia', 'Michał', "Tadek"]
wiek = [47, 67, 32, 34]

# for i in ludzie:
#     print(i, wiek[ludzie.index(i)]) # IndexError: list index out of range
#     # gdy różne długości list mamy błąd

# zip() - łączy kolekcje
for l, w in zip(ludzie, wiek):
    print(l, w)

zipped = zip_longest(ludzie, wiek, fillvalue='Nan')
print(type(zipped))  # <class 'itertools.zip_longest'>
zipped_list = list(zipped)

for item in zipped_list:
    print(item)  # ('Tadek', 'Nan')

print(zipped)  # <itertools.zip_longest object at 0x0000028458144C70>
print("Zaczynam drugą pętlę")
for name, age in zipped_list:
    print(name, age)
# ctrl / - komentowanie linii

c = {'name': 'Radek', 'age': 5}
print({v: k for k, v in c.items()})
# {'Radek': 'name', 5: 'age'}

d = {}
for k, v in c.items():
    d[v] = k
print(d)  # {'Radek': 'name', 5: 'age'}

names = ['John', 'Alice', 'Bob']
ages = [25, 30, 35]
people = [(name, age) for name, age in zip(names, ages)]
print(people)  # [('John', 25), ('Alice', 30), ('Bob', 35)]

