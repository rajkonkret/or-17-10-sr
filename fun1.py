a = 8
b = 7


# funkcja  - wydzielony fragment programu, który można wykonać wielokrotnie
# funkcja najpierw musi byc zdefiniowana, potem dopiero może byc uzyta

def dodaj():  # definicja funkcji (bezargumentowa)
    print(a + b)


def dodaj2(a, b):  # funkcja z argumentami obowiązkowymi
    print(a + b)


def dodaj3(a, b, c=0):  # funkcja z trzema argumentami, trzeci ma domyslną wartośc. symulujemy przeciązanie
    print(a + b + c)


def mnozenie(a, b):  # funkcja zwracająca wynik (return)
    return a * b


dodaj()  # uruchumienie funkcji
# nazwa funkcji i nawiasy ()
dodaj2(4, 5)
dodaj3(1, 2)
dodaj3(6, 7, 8)
dodaj3(c=7, b=0, a=9)  # argumenty po nazwie
dodaj3(1, c=0, b=9)
print(dodaj())  # None - nic nie zwraca
# print(dodaj() + dodaj2(6, 7))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
print(mnozenie(6, 7))  # 42
wyn = mnozenie(8, 9)
print(wyn + mnozenie(12, 17))  # 276
