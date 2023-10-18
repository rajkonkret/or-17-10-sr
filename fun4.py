# napisaniu funkcji, ktora za pomoca prekazanych argumentów stworzy słownik
# first, last, age
def build_person(first, last, age=None):
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age

    return person


while True:
    print("Podaj imię i nazwisko")
    print("Wpisz q by zakończyć")
    f_name = input("Imię: ")
    if f_name == 'q':
        break
    l_name = input("Nazwisko: ")
    if l_name == 'q':
        break
    age = input("Wiek: ")
    if age == 'q':
        break
    print(build_person(f_name, l_name, age))
