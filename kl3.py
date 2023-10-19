# dziedziczenie klas
from pprint import pprint


class Contact:
    all_contacts = []  # pusta lista

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)  # dopisanie kontaktów do listy

    def __repr__(self):
        return f'{self.name!r}, {self.email!r}'


class Suplier(Contact):
    """
    Dziedziczy po Contact
    """

    # pass
    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


c1 = Contact("Adam", "admin@wp.pl")
c2 = Contact("Radek", "admin1@wp.pl")
c3 = Contact("Krzys", "admin2@wp.pl")
c4 = Contact("Arek", "admi4n@wp.pl")
print(c1)
print(c1.all_contacts)
# [Adam, admin@wp.pl, Radek, admin1@wp.pl, Krzys, admin2@wp.pl, Arek, admi4n@wp.pl]
# ['Adam', 'admin@wp.pl', 'Radek', 'admin1@wp.pl', 'Krzys', 'admin2@wp.pl', 'Arek', 'admi4n@wp.pl']
# !r Adam -> 'Adam'
s = Suplier("Tomasz", "tomasz@wp.pl")
print(s)  # 'Tomasz', 'tomasz@wp.pl'
print(s.all_contacts)
s.order("kawa")  # kawa zamówiono od Tomasz
pprint(c1.all_contacts)
# ['Adam', 'admin@wp.pl',
#  'Radek', 'admin1@wp.pl',
#  'Krzys', 'admin2@wp.pl',
#  'Arek', 'admi4n@wp.pl',
#  'Tomasz', 'tomasz@wp.pl']
