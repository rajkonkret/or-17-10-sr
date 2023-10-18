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