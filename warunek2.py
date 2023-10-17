# match case
informacje_o_ksiazce = {
    'autor': input("Podaj autora książki"),
    'tytul': input("Podaj tytuł ksiązki"),
    'rok_wydania': int(input("Podaj rok wydania książki: "))
}

status = ""
match informacje_o_ksiazce['autor'].lower():
    case "tolkien" | "rowling":
        status = "bestseller"
    case "sapkowski" | "luk":
        status = "popularne"
    case "lem" | "asimov":
        status = "klasyka science fiction"
    case _:  # wartość domyślna
        status = "nieznany"

print(f"Książka '{informacje_o_ksiazce['tytul']}' to {status}")
