from storage import load_habits
from habit_service import add_habit, delete_habit, mark_habit, stat_habit

def show_menu():
    print("1: добавление привычки")
    print("2: удаление привычки")
    print("3: отметить привычку")
    print("4: статистика")
    print("5: выход")

print("привет! это Habit tack")
habits = load_habits()

while True:
    show_menu()
    try:
        user_choice = int(input("ваш выбор: "))
    except ValueError:
        print("пожалуйста введите цифру \n")
        continue
    match user_choice:
        case 1:
            add_habit(habits)
        case 2:
            delete_habit(habits)
        case 3:
            mark_habit(habits)
        case 4:
            stat_habit(habits)
        case 5:
            break
        case _:
            print("повторите запрос")
