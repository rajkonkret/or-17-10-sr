lista = []  # pusta lista
print(lista)
print(type(lista))  # <class 'list'>

lista.append("Radek")  # dodawanie do listy
print(lista)  # ['Radek']

lista.append("Tomek")
lista.append("Asia")
lista.append("Renata")
lista.append("Darek")
lista.append("Paweł")
lista.append("Marcin")
print(lista)  # ['Radek', 'Tomek', 'Asia', 'Renata', 'Darek', 'Paweł', 'Marcin']
# lista achowuje kolejność dodawnia

print(lista[1])
# nazwa listy, nawias [], numer indeksu
# indeksowanie od 0, czyli pierwszy element ma indeks 0
# print(lista[10])  # IndexError: list index out of range

lista[1] = "Magda"
print(lista)  # ['Radek', 'Magda', 'Asia', 'Renata', 'Darek', 'Paweł', 'Marcin']

lista.insert(1, "Lukasz")
print(lista)  # ['Radek', 'Lukasz', 'Magda', 'Asia', 'Renata', 'Darek', 'Paweł', 'Marcin']

print(len(lista))  # 8

lista.append("Asia")
print(lista)
lista.remove("Asia")  # usuniecie pierwszeg napotkanego elementu z listy
print(lista)

element_index = lista.index('Renata')
print(lista.pop(element_index))  # Renata
print(lista)

a = 1
b = a
print(a, b)
a = 7
print(a, b)  # 7 1
lista_copy = lista  # skopiowalismy referencje ( miejsce w pamieci)
lista2 = lista.copy()  # skopiowanie listy do nowej listy (w nowe miejsce pamięci)
print(lista)
print(lista_copy)
lista.clear()  # kasowanie wszystkich elemntów listy
print(lista)
print(lista_copy)
print(id(lista))  # 2770985865472
print(id(lista_copy))  # 2770985865472
print(lista2)  # ['Radek', 'Lukasz', 'Magda', 'Darek', 'Paweł', 'Marcin', 'Asia']
print(id(lista2))  # 2271678870656

liczby = [54, 999, 34, 22, 12.34, 876]
# liczby = [54, 999, 34, 22, 12.34, 876, "A"]  # TypeError: '<' not supported between instances of 'str' and 'int'
print(liczby)
liczby.sort()
print(liczby)
print(lista.copy().__doc__)  # wyswietlenie dokumentacji
# Built-in mutable sequence.
#
# If no argument is given, the constructor creates a new empty list.
# The argument must be an iterable if specified.
liczby.reverse()
print(liczby)  # [999, 876, 54, 34, 22, 12.34]
liczby2 = liczby.copy()
print(liczby2)
liczby.clear()
print(liczby2)

print(liczby2[:3])  # od indeksu 0 do 2
print(liczby2[2:])  # od indeksu 2 włacznie do końca włącznie
print(liczby2[:-1])  # -1 (ostatni) od 0 do -1 (bez -1) czyli do przedostatniego, [999, 876, 54, 34, 22]
print(liczby2[-1])  # element ostatni 12.34

#  Radek
#  01234
# -(54321) - ujemne indeksy
print(liczby2[:-2])  # [999, 876, 54, 34]
print(len(liczby2))  # 6
liczby2.remove(54)
print(liczby2)
# liczby.remove(54)  # ValueError: list.remove(x): x not in list
print(liczby2)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
# lista1.append(lista2)  # [1, 2, 3, [4, 5, 6]]
lista1.extend(lista2)
print(lista1)  # [1, 2, 3, 4, 5, 6]

lista3 = ['a', 'b', 'c']
napis = 'def'
lista3.extend(napis)
print(lista3)  # ['a', 'b', 'c', 'd', 'e', 'f']
lista3.append(napis)  # ['a', 'b', 'c', 'd', 'e', 'f', 'def']
print(lista3)
wart = [1, 2, 3]
lista3.append(wart)
print(lista3)  # ['a', 'b', 'c', 'd', 'e', 'f', 'def', [1, 2, 3]]
lista3.extend(wart)
print(lista3)  # ['a', 'b', 'c', 'd', 'e', 'f', 'def', [1, 2, 3], 1, 2, 3]
tekst = 'Python'
lista_z_tekstu = list(tekst)  # rzutowanie na liste
print(lista_z_tekstu)  # ['P', 'y', 't', 'h', 'o', 'n']
lista_2 = [tekst]
print(lista_2)  # ['Python']

krotka = tuple(liczby2)  # rzutowanie listy na tuple(krotke)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # (999, 876, 34, 22, 12.34)
