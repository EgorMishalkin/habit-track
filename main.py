habits = {"python": 3, "xd": 2}

def show_menu():
    print("1: добавление привычки")
    print("2: удаление привычки")
    print("3: отметить привычку")
    print("4: статистика")
    print("5: выход")

def show_habits():
    if not habits:
        print("привычек пока нет")
    else:
        print("список привычек:", *habits, sep=", ")

def add_habit():
    habit = input("напиши название привычки которую добавить: ")
    if habit in habits:
        print("Такая привычка уже есть")
    else:
        habits[habit] = 0
        print("Привычка добавлена")

def delete_habit():
    show_habits()
    habit = input("напиши название привычки которую удалить: ")
    # я сначала написал habits.keys, но можно просто habits
    if habit not in habits:
        print("Привычка нет такой")
    else:
        del habits[habit]
        print("Привычка удалена")

def mark_habit():
    show_habits()
    habit = input("напиши название привычки которую хотите отметить: ")
    if habit not in habits:
        print("Привычка нет такой")
    else:
        habits[habit] += 1
        print(f"количество обновлено! красавчик нах. количество {habits[habit]}")

def stat_habit():
    if not habits:
        print("Привычек пока нет")
    else:
        for key, value in habits.items():
            print(f"{key}: {value}")

print("привет! это Habit tack")

while True:
    show_menu()
    try:
        user_choice = int(input("ваш выбор: "))
    except ValueError:
        print("пожалуйста введите цифру \n")
        continue
    match user_choice:
        case 1:
            add_habit()
        case 2:
            delete_habit()
        case 3:
            mark_habit()
        case 4:
            stat_habit()
        case 5:
            break
        case _:
            print("повторите запрос")
