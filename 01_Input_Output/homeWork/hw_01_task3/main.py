# Семинар 1
# Домашняя работа
# Задание 3 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти.

def main():
    quarterInt = get_console_input_int("Please enter quarter within 1...4 range")
    try:
        print(get_quarter_range_str(quarterInt))
    except Exception as exc:
        print(exc)


def get_quarter_range_str(quarterInt):
    match quarterInt:
        case 1:
            return "x > 0; y > 0"
        case 2:
            return "x > 0; y < 0"
        case 3:
            return "x < 0; y < 0"
        case 4:
            return "x < 0; y > 0"
        case _:
            raise Exception("Argument out of 1...4 range")


def get_console_input_int(requestTextStr):
    while True:
        try:
            return int(input(f'{requestTextStr}: '))
        except ValueError:
            print("You have entered not a =n integer value. Please try again.")


main()
