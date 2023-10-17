# for - petla iteracyjna

lista = []

for i in range(6):  # 0..5
    print(i)
    if i % 2 == 0:
        print("Jest parzysta", i, end='', sep=";")
        lista.append(i)

print(lista)  # [0, 2, 4]
lista2 = [j for j in range(6) if j % 2 == 0]  # [j] - odpowiednik append
print(lista2)
lista3 = [j if j % 2 == 0 else 10 for j in range(6)]
print(lista3)  # [0, 10, 2, 10, 4, 10]

for c in lista2:
    if c == 2:
        c += 1  # c = c + 1
    print(c)  # 3

# +=, -=, *=, /=, %=
a = 1
a += 1  # a = a + 1
print(a)
a -= 3  # a = a - 3
print(a)
a *= 2  # a = a * 2
print(a)
a /= 2  # a = a / 2
print(a)  # -1.0
# dzielenie daje wynik float
a %= 2
print(a)  # 1.0
