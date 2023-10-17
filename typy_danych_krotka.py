# krotka - kolekcja, niezmienna
# po utworzeniu nie można zmienić tej kolekcji, czyli nie mozna do niej dodawac i usuwac elementów
# indexy liczone od 0
tupla = "Tomek", "Michał", "Asia", "Daniel"
print(tupla)  # ('Tomek', 'Michał', 'Asia', 'Daniel')
print(type(tupla))  # <class 'tuple'>
tupla2 = ("Radek",)
print(type(tupla2))  # <class 'tuple'>
print(tupla2)  # ('Radek',)
tupla3 = 44, 34, 22.43, 11, 200

print(tupla3)
print(type(tupla3))  # <class 'tuple'>

print(tupla.index("Tomek"))
print(tupla.count('Asia'))  # zlicza ilosc wystąpień elementu

asia = tupla[2]
print(asia)  # Asia
# tupla[0] = "Radek"  # TypeError: 'tuple' object does not support item assignment

# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\or-17-10-sr\typy_danych_krotka.py", line 20, in <module>
#     tupla[0] = "Radek"
#     ~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
# ('Tomek', 'Michał', 'Asia', 'Daniel')

a, b = 1, 2  # rozpakowanie tupli
print(a, b)
a, *b = 1, 2, 3
print(a)
print(b)  # [2, 3] - worek na pozostałe
# ('Tomek', 'Michał', 'Asia', 'Daniel')
imie1, *imie2, imie3 = tupla
print(imie1)
print(imie2)  # ['Michał', 'Asia']
print(imie3)
print(type(imie2))

lista = list(tupla)
print(lista)  # ['Tomek', 'Michał', 'Asia', 'Daniel']
print(type(lista))  # <class 'list'>
# 13:30
