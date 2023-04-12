# Семинар 1
# Задача 3 Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N


def main():
    value = abs(get_console_input_int("Please enter integer value"))
    counter = value * (-1)
    while value >= counter:
        print(counter, end=' ')
        counter += 1


def get_console_input_int(requestTextStr):
    while True:
        try:
            return int(input(f'{requestTextStr}: '))
        except ValueError:
            print("You have entered not a =n integer value. Please try again.")


main()
