from typing import Optional


class Sample:
    def __init__(
            self,
            a: int,
            b: int,
            c: int,
            d: int,
            e: Optional[str] = None) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def __repr__(self):
        if self.e is None:
            self.e = 'nieznane'
        return (
            f'a = {self.a}, '
            f'b = {self.b}, '
            f'c = {self.c}, '
            f'd = {self.d}, '
            f'e = {self.e} '
        )


ob = Sample(1, 2, 3, 4, 5)
print(ob)
ob2 = Sample(1, 2, 3, 4)
print(ob2)
