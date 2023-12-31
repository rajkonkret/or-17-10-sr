def uppercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()

    return wrapper


def bold_decorator(function):
    def wrapper():
        result = function()
        return f"\033[1m" + "Tekst" + "\033[0m"

    return wrapper


@bold_decorator
@uppercase_decorator
def greeting():
    return "Hello, World!"


print(greeting())  # HELLO, WORLD!, Tekst
