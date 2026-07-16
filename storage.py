import json

def load_habits():
    # Открываем файл для чтения
    try:
        with open("habits.json", "r", encoding="utf-8") as f:
            # Загружаем данные из файла в переменную
            habits_data = json.load(f)
            return habits_data
    except FileNotFoundError:
        print("файл не найден =(")

def save_habits(habits):
    # Writing JSON data to a file
    with open("habits.json", "w", encoding="utf-8") as file:
        json.dump(habits, file, ensure_ascii=False, indent=4)