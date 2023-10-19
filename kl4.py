class ContactList(list['Contact']):

    def search(self, name):
        matchng_contacts = []
        for c in self:
            if name in c.name:
                matchng_contacts.append(c)
        return matchng_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f'{self.name!r}, {self.email!r}'


class Suplier(Contact):
    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


class Friend(Suplier, Contact):
    """
    dziedziczy po klasie Suplier i Contact
    """

    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

    def order(self, order):
        # super(Friend, self).order(order)
        # Suplier.order(self, order)
        print("To ja", self.name, f"{order}")

    def __repr__(self):
        return f"{self.name!r}, {self.email!r}, +48 {self.phone!r}"


cl = ContactList()
print(cl)
cl.append("e")
print(cl)
c1 = Contact("Adam", "adam@wp.pl")
print(c1)  # 'Adam', 'adam@wp.pl'

s = Suplier("Radek", "radek@wp.pl")
s.order("kawa")
print(s.all_contacts)  # ['Adam', 'adam@wp.pl', 'Radek', 'radek@wp.pl']
print(s.all_contacts.search('Adam'))  # ['Adam', 'adam@wp.pl']
# 11:30
f = Friend("Jarek", "jarek@wp.pl", "66666666")
print(f)  # 'Jarek', 'jarek@wp.pl'
print(Friend.__mro__)  # sprawdzenie kolejnsci rozwiązywania nazw
# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
f.order("herbata")
print(f)
print(f.all_contacts)  # ['Adam', 'adam@wp.pl', 'Radek', 'radek@wp.pl', 'Jarek', 'jarek@wp.pl', +48 '66666666']
