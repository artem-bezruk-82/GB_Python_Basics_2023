# Семинар 2
# Домашняя работа
# Задание 1
# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.

def main():
    factorials = list()
    valueInt = abs(get_console_input_int("Please enter integer value"))
    for i in range(1, valueInt + 1):
        factorials.append(get_factorial(i))
    print(factorials)


def get_factorial(valueInt):
    factorial = 1
    for i in range(1, valueInt + 1):
        factorial *= i
    return factorial


def get_console_input_int(requestTextStr):
    while True:
        try:
            return int(input(f'{requestTextStr}: '))
        except ValueError:
            print("You have entered not a =n integer value. Please try again.")


main()
