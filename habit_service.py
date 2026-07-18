from storage import save_habits
from datetime import date

def show_habits(habits):
    if not habits:
        print("привычек пока нет")
    else:
        print("список привычек:", *habits, sep=", ")

def add_habit(habits):
    show_habits(habits)
    habit = input("напиши название привычки которую добавить: ")
    if habit in habits:
        print("Такая привычка уже есть")
    else:
        habits[habit] = []
        save_habits(habits)
        print("Привычка добавлена")

def delete_habit(habits):
    show_habits(habits)
    habit = input("напиши название привычки которую удалить: ")
    # я сначала написал habits.keys, но можно просто habits
    if habit not in habits:
        print("Привычка нет такой")
    else:
        del habits[habit]
        save_habits(habits)
        print("Привычка удалена")

def mark_habit(habits):
    show_habits(habits)
    habit = input("напиши название привычки которую хотите отметить: ")
    today = str(date.today())
    if habit not in habits:
        print("Привычка нет такой")
    else:
        if today in habits[habit]:
            print('привычка сегодня уже отмечена!')
        else:
            habits[habit].insert(0, today)
            save_habits(habits)
            print(f"количество обновлено! красавчик нах. количество {len(habits[habit])}")

def stat_habit(habits):
    if not habits:
        print("Привычек пока нет")
    else:
        for key, value in habits.items():
            if not value:
                print(f'привычка: {key}')
                print(f"количество выполнений: 0")
            else:
                print(f'привычка {key}')
                print(f"количество выполнений: {len(value)}")
                print(f"последнее выполнение: {value[0]}")