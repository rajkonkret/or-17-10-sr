# role = "manager"
# permissions = ['modify_finances']

role = "employee"
permissions = ['view_reports']
resource = input("Podaj nazwę zasobu, do którego chcesz mieć dostęp: ")

if role == "admin":
    print("Dostęp przyznany")
elif role == "manager":
    if resource in ['reports', 'data', 'users']:
        print("Dostęp przyznany")
    elif "modify_finances" in permissions and resource == "finances":
        print("Dostęp przyznany")
    else:
        print("Dostęp zabroniony")
elif role == "employee":
    if resource == "data":
        print("Dostęp przyznany")
    elif "view_reports" in permissions and resource == "reports":
        print("Dostęp przyznany")
    else:
        print("Dostęp zabroniony")
elif role == "intern":
    if f"access_{resource}" in permissions:
        print("Dostęp przyznany")
    else:
        print("Dostęp zabroniony")
else:
    print("Nieznana rola. Dostęp zabroniony")
