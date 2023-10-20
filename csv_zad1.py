# pliki csv - pliki w ktorych dane są oddzielone znakiem podziału
# , ; tab
# Radek, Michał, Zenek
import csv

fields = ["name", "branch", "year", "cgpa"]

my_dict = [
    {'branch': "COE", 'cgpa': 9.1, 'name': "radek", "year": 3},
    {'branch': "COk", 'cgpa': 9, 'name': "MArek", "year": 2},
    {'branch': "COs", 'cgpa': 8.1, 'name': "Zenek", "year": 1},
    {'branch': "COL", 'cgpa': 9.11, 'name': "Tomek", "year": 0},
]

filename = 'records.csv'
with open(filename, "w", encoding="utf-8", newline='') as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(my_dict)

new_fields = []
new_rows = []

with open(filename, "r", encoding="utf-8", newline="") as csv_f:
    csvreader = csv.reader(csv_f)
    # csvreader = csv.DictReader(csv_f)
    new_fields = next(csvreader)  # odczytanie wiersza o indeksi 0,
    # wpisanie do zmiennej i ustawienie wskażnika na nstępny
    for row in csvreader:  # ta pętla wystartuje od indeksu 1
        new_rows.append(row)

print(new_fields)
print(new_rows)
# ['name', 'branch', 'year', 'cgpa']
# [['radek', 'COE', '3', '9.1'], ['MArek', 'COk', '2', '9'],
# ['Zenek', 'COs', '1', '8.1'], ['Tomek', 'COL', '0', '9.11']]

new_dict = []

with open(filename, "r", encoding='utf-8', newline="") as c:
    csvreader = csv.DictReader(c)
    for row in csvreader:
        print(row)
        new_dict.append(row)

print(new_dict)
for i in new_dict:
    print(i)  # {'name': 'Tomek', 'branch': 'COL', 'year': '0', 'cgpa': '9.11'}

