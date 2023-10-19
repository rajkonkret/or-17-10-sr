from abc import ABC, abstractmethod


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    @abstractmethod  # oznaczenie metody abstrakcyjnej
    def drukuj(self):
        pass

    def increment(self, by=1):
        self.values += by

    @classmethod
    def from_counter(cls, counter):
        return cls(counter.values)

    @staticmethod  # metoda statyczna, można uzyc nie tworząc obiektu (instancji) klasy
    def format_string():
        return '%d'


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values=0):
        if values > self.MAX:
            raise ValueError("Wartość nie może przekroszyć MAX")
        super(BoundedCounter, self).__init__(values)

    def drukuj(self):
        print("Drukuje...", self.values)


# po dodaniu @abstractmethod
# TypeError: Can't instantiate abstract class Counter without an
# implementation for abstract method 'drukuj'

# c = Counter()
# c.increment()
# print(c)
# c.drukuj()  # wydrukowało nic bo metoda pass
b = BoundedCounter()
b.increment()
b.drukuj()
c = BoundedCounter()
c.drukuj()
d = BoundedCounter.from_counter(b)
d.drukuj()
print(d.format_string())
print(BoundedCounter.format_string())