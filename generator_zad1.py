def kwadrat(n):
    for x in range(n):
        print(x ** 2)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # wykonaj działanie i zapamiętaj gdzie zakońćzyłeś


kwadrat(5)
kwa = kwadrat2(5)
print(kwa)  # <generator object kwadrat2 at 0x0000028F500FF780>
print(type(kwa))  # <class 'generator'>

print(next(kwa))  # 0
print(next(kwa))
print(next(kwa))
print(next(kwa))  # 9
print("Wypisz cokolwiek")
print("Zrobic cokolwiek")
lista = []
lista.append("12343564367567")
print(next(kwa))

# print(next(kwa))  # StopIteration
kwa2 = kwadrat2(6)
print(next(kwa2))
