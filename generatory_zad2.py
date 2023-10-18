generator_1 = (x for x in [1, 2, 3, 5])
print(type(generator_1))  # <class 'generator'>

print(next(generator_1))
print(next(generator_1))


def generator2():
    i = 1
    while True:
        yield i * i
        i += 1


def fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


def fibo_with_index(n):
    a, b = 0, 1
    for idx in range(n):
        yield idx, a
        a, b = b, a + b


# x = idx, a - tupla(krotka)


g = generator2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

fib = fibo()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

fib2 = fibo()
print(next(fib2))
# 14:55

for i in fibo_with_index(10):
    print(f"element: {i} ")  # element: (9, 34)

for i, n in fibo_with_index(10):
    print(f"Pozycja: {i}: {n}")


def counter(start=0):
    n = start
    while True:
        result = yield n
        print(result)
        if result == 'q':
            break
        n += 1


c = counter(10)
print(next(c))
print(next(c))
print(next(c))
print(c.send('OK'))  # OK
try:
    print(c.send('q'))
# print(next(c))  # StopIteration
except StopIteration:
    print("Generator zakończył działanie")
