import json
import os
import random

FILENAME = "game_stats.json"

def load_stats():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return {"games_played": 0, "wins": 0, "losses": 0}

def save_stats(stats):
    with open(FILENAME, "w") as f:
        json.dump(stats, f, indent=4)

def update_stats(win: bool):
    stats = load_stats()
    stats["games_played"] += 1
    if win:
        stats["wins"] += 1
    else:
        stats["losses"] += 1
    save_stats(stats)

def play_game():
    try:
        user_number = int(input("Введіть своє число (від 1 до 100): "))
        if not 1 <= user_number <= 100:
            print("Число має бути від 1 до 100!")
            return
        comp_number = random.randint(1, 100)
        print(f"Число комп'ютера: {comp_number}")
        if user_number > comp_number:
            print("Ви виграли!")
            update_stats(True)
        else:
            print("Ви програли!")
            update_stats(False)
    except ValueError:
        print("Це не число!")

play_game()
print("Поточна статистика:", load_stats())
