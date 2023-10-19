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
