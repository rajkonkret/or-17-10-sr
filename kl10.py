import pickle
from kl9 import Person

with open('dane.txt', 'r') as stream:
    p2 = stream.read()

print(p2)
print(type(p2))  # <class 'str'>

with open('data.pickle', 'rb') as stream:
    p = pickle.load(stream)

print(p)
print(type(p))  # <class 'list'>
for person in p:
    person.greet()
    sd = pickle.dumps(person)
    # b'\x80\x04\x95L\x00\x00\x00\x00\x00\x00\x00\x8c\x03kl9\x94\x8c\x06Person\x94\x93\x94)\x81\x94}\x94(\x8c\nfirst_name\x94\x8c\x07Mateusz\x94\x8c\tlast_name\x94\x8c\x05Zegar\x94\x8c\x02id\x94K\x02ub.'
    print(sd)  # zserializowany obiekt
    print(pickle.loads(sd))  # zdeserializowany obiekt Person(first_name='Mateusz', last_name='Zegar', id=2)
