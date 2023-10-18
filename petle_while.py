# while - petla sterowana warunkiem

licznik = 0
while True:
    licznik += 1
    print("Komunikat")
    if licznik > 10:
        break  # przerwanie działąnia pętli

licznik = 0
while licznik < 10:
    print("Komunikat2")
    licznik += 1

lista = []
while True:  # często jest stosowana jako główna pętla programu
    wej = input("Podaj liczbe")  # str
    if not wej.isnumeric():
        break
    lista.append(int(wej))

print(lista)