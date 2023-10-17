czy_znasz_Python = False

if czy_znasz_Python:
    print("Super")  # wciecie obowiazkowe
else:
    print("Musisz się dalej uczyć")

print("Dalsza część programu")

if czy_znasz_Python:
    pass  # nic nie rób

print("Dalsza część 2")

name = "Tomek"
if name == "Radek":  # == przyrównanie
    print(f"Twoje imię {name}")

# := przypisz wartosc do zmiennej i porównaj
if name := "Radek":
    print(f"Twoje imię {name}")

name = "Radek"
if name == "Radek":
    print("ok")

word_len = len(name)
if word_len > 2:
    print("Długość ok")

if (word_len := len(name)) > 2:
    print(f"Długość ok 2 {word_len}")

typ_samochodu = "pieszo"
wiek = int(input("Podaj swój wiek: "))

if wiek < 18:
    typ_samochodu = 'pieszo'
elif wiek < 25:
    typ_samochodu = 'samochod sportowy'
elif wiek < 60:
    typ_samochodu = "mały samochod"
else:
    typ_samochodu = 'kabriolet'

print(f"Na podstawie Twojego wieku sugeruję: {typ_samochodu}")
# dodac warunek, gdzie dla wieku 25 do 59 zaproponujemy mały samochód
# kolejnosc ma znaczenie
# po wejsciu w jeden z warunków po wykonaniu instrukcji wychodzi do głownego programu
#
