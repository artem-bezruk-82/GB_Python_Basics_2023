# Семинар 2
# Домашняя работа
# Задание 1
# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.

def main():
    factorials = list()
    valueInt = abs(get_console_input_int("Please enter integer value"))
    iteration = 1
    while iteration <= valueInt:
        factorials.append(get_factorial(iteration))
        iteration += 1
    print(factorials)


def get_factorial(valueInt):
    factorial = 1
    iteration = 1
    while iteration <= valueInt:
        factorial *= iteration
        iteration += 1
    return factorial


def get_console_input_int(requestTextStr):
    while True:
        try:
            return int(input(f'{requestTextStr}: '))
        except ValueError:
            print("You have entered not a =n integer value. Please try again.")


main()
