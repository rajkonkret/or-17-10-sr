def example(a, b, /, d=0, **kwargs):  # ** - argumenty słownikowe
    print(a, b, d)
    print(kwargs)  # {}
    return a * b


print(type(example))
print(example.__code__.co_varnames)  # ('a', 'b', 'kwargs')
print(example(1, 2))
print(example(1, 2, l=8))  # {'l': 8}
print(example(1, 2, c="Radek", l=8))  # {'c': 'Radek', 'l': 8}
# po dodaniu w argumentach /
# print(example(1, b=3))  # TypeError: example() missing 1 required positional argument: 'b'
print(example(1, 2, b=9))  # {'b': 9}
# / - odddziela arguemty pozycyjne od nazwanych
print(example(1, 2, d=10))  # 1 2 10


# lambda - skrocony zapis funkcji, mozebyc zdefiniowana funkcja w miejscu wywołania
def liczymy(x, y):
    return x * y


liczymy = lambda x, y: x * y  # lambda ma return standardowo

print(liczymy(200, 50))  # 10000

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 55]
# map()
print(f"Użycie map() {list(map(lambda x: x * 2, lista))}")  # lambda jako funkcja anonimowa
# Użycie map() [2, 4, 6, 8, 10, 12, 14, 16, 18, 40, 110]

# filter() - filtruje dane na podstawie funkcji z warunkiem
print(f"Użycie filter(): {list(filter(lambda x: x < 5, lista))}")  # Użycie filter(): [1, 2, 3, 4]

r0 = {'miasto': 'Kielce'}
r1 = {'miasto': 'Kielce', 'ZIP': "25-900"}
print(r0['miasto'])
print(r1['miasto'])
print(r1['ZIP'])
# print(r0['ZIP'])  # KeyError: 'ZIP'
d_zip = lambda row: row.setdefault('ZIP', '00-000')
print(d_zip(r0))
print(r0)  # {'miasto': 'Kielce', 'ZIP': '00-000'}
print(d_zip(r1))  # 25-900
print(r1)  # {'miasto': 'Kielce', 'ZIP': '25-900'}
r1.setdefault("Test", "1")
print(r1)  # {'miasto': 'Kielce', 'ZIP': '25-900', 'Test': '1'}

lata = [(2000, 29.97), (2001, 33.12), (2010, 32.92)]
print(max(lata))  # (2010, 32.92)
print(max(lata, key=lambda c: c[1]))  # (2001, 33.12)
print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))
# (c[1], c) => (33.12, (2001, 33.12))
# 13:25
