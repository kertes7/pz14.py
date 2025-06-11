import json
import os

FILENAME = "clients.json"

def load_clients():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_clients(clients):
    with open(FILENAME, "w") as f:
        json.dump(clients, f, indent=4)

def add_client():
    name = input("Введіть ім'я клієнта: ")
    email = input("Введіть email клієнта: ")
    phone = input("Введіть телефон клієнта: ")
    clients = load_clients()
    clients.append({"name": name, "email": email, "phone": phone})
    save_clients(clients)
    print("Клієнта додано.")

def find_client():
    name = input("Введіть ім'я для пошуку: ")
    clients = load_clients()
    found = [c for c in clients if c["name"].lower() == name.lower()]
    if found:
        for c in found:
            print(f"{c['name']} | {c['email']} | {c['phone']}")
    else:
        print("Клієнта не знайдено.")

def update_client():
    name = input("Введіть ім'я клієнта для оновлення: ")
    clients = load_clients()
    for c in clients:
        if c["name"].lower() == name.lower():
            print(f"Поточна інформація: {c}")
            c["email"] = input("Новий email: ")
            c["phone"] = input("Новий телефон: ")
            save_clients(clients)
            print("Дані оновлено.")
            return
    print("Клієнта не знайдено.")

def delete_client():
    name = input("Введіть ім'я клієнта для видалення: ")
    clients = load_clients()
    new_clients = [c for c in clients if c["name"].lower() != name.lower()]
    if len(new_clients) != len(clients):
        save_clients(new_clients)
        print("Клієнта видалено.")
    else:
        print("Клієнта не знайдено.")

def menu():
    while True:
        print("\n=== Меню бази клієнтів ===")
        print("1. Додати клієнта")
        print("2. Знайти клієнта")
        print("3. Оновити клієнта")
        print("4. Видалити клієнта")
        print("5. Показати всіх клієнтів")
        print("0. Вихід")
        choice = input("Ваш вибір: ")
        if choice == "1":
            add_client()
        elif choice == "2":
            find_client()
        elif choice == "3":
            update_client()
        elif choice == "4":
            delete_client()
        elif choice == "5":
            for c in load_clients():
                print(f"{c['name']} | {c['email']} | {c['phone']}")
        elif choice == "0":
            break
        else:
            print("Невірний вибір!")

menu()
