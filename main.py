habits = {}

def show_menu():
    print("1: добавление привычки")
    print("2: удаление привычки")
    print("3: отметить привычку")
    print("4: статистика")
    print("5: выход")

def add_habit():
    habit = input("напиши название привычки которую добавить: ")
    if habit in habits.keys():
        print("Привычка есть")
    else:
        habits[habit] = 0

def del_habit():
    habit = input("напиши название привычки которую удалить: ")
    # я сначала написал habits.keys, но можно просто habits
    if habit not in habits:
        print("Привычка нет такой")
    else:
        del habits[habit]

def mark_habit():
    habit = input("напиши название привычки которую хотите отметить: ")
    if habit not in habits.keys():
        print("Привычка нет такой")
    else:
        habits[habit] += 1

def stat_habit():
    for key, value in habits.items():
        print(f"{key}: {value}")

print("привет! это Habit tack")

while True:
    show_menu()
    user_choice = int(input("ваш выбор: "))
    match user_choice:
        case 1:
            add_habit()
        case 2:
            del_habit()
        case 3:
            mark_habit()
        case 4:
            stat_habit()
        case 5:
            break
        case _:
            print("повторите запрос")
