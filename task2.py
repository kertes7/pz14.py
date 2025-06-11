import json

FILENAME = "contacts.json"

def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent=4)

def load_contacts():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def add_contact():
    contacts = load_contacts()
    name = input("Введіть ім'я контакту: ")
    phone = input("Введіть номер телефону: ")
    email = input("Введіть електронну пошту: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Контакт додано успішно!")

def show_contacts():
    contacts = load_contacts()
    if not contacts:
        print("Контакти відсутні.")
        return
    for name, info in contacts.items():
        print(f"{name}: Телефон: {info['phone']}, Email: {info['email']}")

add_contact()
show_contacts()

