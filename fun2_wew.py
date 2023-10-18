def f():
    print("Funkcja 1")

    def fwew(a, b):
        return a * b

    return fwew  # bez nawiasów bo zwracamy tylko adres funkcji a nie wynik działania


x = f()
print(type(x))  # <class 'function'>
print(x)  # <function f.<locals>.fwew at 0x0000018E45D69760>
# nazwa funkcji i nawiasy ()
print(x(6, 7))  # 42
