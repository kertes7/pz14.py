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

def add_client(name, email):
    clients = load_clients()
    clients.append({"name": name, "email": email})
    save_clients(clients)

def find_client(name):
    return [c for c in load_clients() if c["name"].lower() == name.lower()]

def update_client(name, new_email):
    clients = load_clients()
    for c in clients:
        if c["name"].lower() == name.lower():
            c["email"] = new_email
            break
    save_clients(clients)

def delete_client(name):
    clients = load_clients()
    clients = [c for c in clients if c["name"].lower() != name.lower()]
    save_clients(clients)

add_client("Олег", "oleg@email.com")
print(find_client("Олег"))
update_client("Олег", "newemail@ukr.net")
print(find_client("Олег"))
delete_client("Олег")
print(load_clients())
