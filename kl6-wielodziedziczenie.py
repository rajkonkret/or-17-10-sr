# podstawy wielodziedziczenia
class A:
    def method(self):
        print("Metoda z kalsa A")


class B:
    def method(self):
        print("Metoda z kalsy B")


class C(A, B):  # kolejnosc ma znacznie, w tym przypadku najpierw szuka w A jesli nie znajdzie w C
    """
    Klasa C, dziedziczy po klasie A i B
    """

    def method(self):
        # super() - oznacza użycie elementu z klasy wyższej
        super().method()  # Metoda z kalsa A, bo A na pierwszym miejscu
        print(f"Metoda z klasy C")  # Metoda z klasy C
        B.method(self)  # Metoda z kalsy B


a = A()
a.method()
b = B()
b.method()
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

c = C()
c.method()
