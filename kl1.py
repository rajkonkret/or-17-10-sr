# klasa  - szablon zawiera wskazanie dla pol i funkcji
# nadanie konkretnych cech  - obiekt
import math

"""
hypot(*coordinates) -> value

Multidimensional Euclidean distance from the origin to a point.

Roughly equivalent to:
    sqrt(sum(x**2 for x in coordinates))

For a two dimensional point (x, y), gives the hypotenuse
using the Pythagorean theorem:  sqrt(x*x + y*y).

For example, the hypotenuse of a 3/4/5 right triangle is:

    >>> hypot(3.0, 4.0)
    5.0
"""

class MyFirstClass:
    """
    Reprezentuje punkty x i y
    """

    def __init__(self, x=0, y=0):
        """
        metoda inicjalizująca
        :param x: x
        :param y: y
        """

        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    # reprezentacja obiektu w sposób czytelny
    def __repr__(self):
        return f"x = {self.x}, y = {self.y}"


# print(MyFirstClass.__doc__)
# print(print.__doc__)

ob = MyFirstClass()
print(ob.x)
ob.move(45, 67)
print(ob)  # <__main__.MyFirstClass object at 0x000001DDF245D520>
# x = 45, y = 67 - po nadpisaniu __repr__
print(ob.__str__())
print(ob.__repr__())
print(ob.y)  # 67
ob.move(0, 0)
ob.reset()
print(ob.x)
a = MyFirstClass(3, 5)
b = MyFirstClass(0, 5)

print(a)  # <__main__.MyFirstClass object at 0x0000022262E5E570>
print(b.calculate(a))
print(a.calculate(b))
assert b.calculate(a) == a.calculate(b)
a.move(3, 4)
print(a.calculate(b))  # 3.1622776601683795
