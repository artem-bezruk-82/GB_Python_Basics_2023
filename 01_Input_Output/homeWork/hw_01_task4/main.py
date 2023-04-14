# Семинар 1
# Домашняя работа
# Задание 4
# Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

def main():
    valueInt = abs(get_console_input_int("Please enter integer value"))
    counter = 1

    while counter <= valueInt:
        if counter % 2 == 0:
            print(counter)
        counter += 1


def get_console_input_int(requestTextStr):
    while True:
        try:
            return int(input(f'{requestTextStr}: '))
        except ValueError:
            print("You have entered not a =n integer value. Please try again.")


main()
