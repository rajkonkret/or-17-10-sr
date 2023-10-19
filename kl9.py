import pickle
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greet(self):
        print(f"Witam, jestem {self.first_name} {self.last_name}, Id to {self.id}")


if __name__ == '__main__':
    people = [
        Person("Jacek", "Kowalski", 1),
        Person("Mateusz", "Zegar", 2)
    ]
    p2 = ("Maciek", "Nowak", "6")
    print(people)  # [Person(first_name='Jacek', last_name='Kowalski', id=1),
    # Person(first_name='Mateusz', last_name='Zegar', id=2)]

    # kontekst menadzera
    with open('dane.txt', 'w') as stream:  # zapisane tekstowo
        stream.write(str(people))

    with open('data.pickle', 'wb') as stream:
        pickle.dump(people, stream)
# 13:30
