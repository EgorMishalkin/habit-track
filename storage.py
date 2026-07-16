import json

def load_habits():
    try:
        with open("habits.json", "r", encoding="utf-8") as f:
            habits_data = json.load(f)
            return habits_data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_habits(habits):
    with open("habits.json", "w", encoding="utf-8") as file:
        json.dump(habits, file, ensure_ascii=False, indent=4)