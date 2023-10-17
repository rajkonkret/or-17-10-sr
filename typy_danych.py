print("Radek")  # wypisz/wydrukuj
# pep8
# ctrl alt l - sformatuje kod

imie = "Radek"  # str czyli typ tekstowy
imie = 'Radek'
print(imie)
# zmienna - takie pudełko na dane
# typowanie dynamiczne
# silne typowanie
wiek = 39
print(wiek)
print(type(wiek))  # <class 'int'>
imie: str = "radek"  # nie jest sprawdzany typ danych
# tylko adnotacja
imie = 39
print(39)
a = 6  # int
b = "7"  # str
print(a * b)  # 777777

wiek = 47
rok = 2023
temp = 36.6  # float zmiennoprzecinkowy
print(0.1 + 0.5)  # 0.6
print((0.1 + 0.7))  # 0.7999999999999999
print(wiek + rok)
print(wiek * rok)
print(wiek - rok)
print(wiek / rok)
print(wiek // rok)  # częśc całkowita z dzielenia, 0
print(wiek % rok)  # modulo, reszta z dzielenia  47
# 5 / 2 = 2 r 1 bo 2 * 2 = 4 + 1 = 5
print(54 - 5 * 43 + 4 / 2 + 4 / 2)
print(54 - (5 * 43) + (4 / 2 + 4) / 2)
a = "7"  # str
b = int(a)  # rzutowanie na int, czyli zamiana str na int
print(int(a) + b)  # 14

print("\tSprawdzam mienną temp: {} {}\n".format(wiek, temp))
print(f"\tSprawdzam zmienna temp {wiek} {temp}")
print(f"""
zmienna {temp}
    zmienna {wiek}""")
imie = "Radek Radek"
print(imie.lower())  # """ Return a copy of the string converted to lowercase. """
print(imie)  # Radek Radek
# stringi są niemutowalne
imie2 = imie.lower()
print(imie2)
print(imie.upper())
print(imie)

# boolean - zmienna logiczna
# True, False
czy_znasz_Pythona = True
print(czy_znasz_Pythona)
czy_znasz_Pythona = False
print(czy_znasz_Pythona)
print(int(True))  # 1
print(int(False))  # 0
print(bool(100))  # rzutowanie na typ boolean - True
print(bool(""))  # False
print(bool("Radek"))  # True
print(bool(-1))  # True
#  komentarz
"""
Komentarz wielolinijkowy
"""
# 11:30
print("imie %s" % "Radek")  # imie Radek
