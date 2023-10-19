class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę calkowitą"))
    if x < 0:
        raise MyException("Liczba musi być dodatnia")
except MyException as e:
    print("Wystąpił mój włąsny wyjątek", e)
except ValueError:
    print("Wystąpił bład wartości")
except Exception as e:
    print("Wystąpił błąd", e)
