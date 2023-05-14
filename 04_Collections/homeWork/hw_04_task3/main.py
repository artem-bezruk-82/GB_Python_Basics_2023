# Семинар 4
# Домашняя работа
# Задача 3
# Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
import math


def main():

    accuracyFloat = abs(get_console_input_float("Please enter accuracy rate using float value within 0...1 range"))
    accuracyInt = 0
    if accuracyFloat <= 0 or accuracyFloat >= 1:
        print(int(math.pi))
    else:
        while accuracyFloat < 1:
            accuracyFloat *= 10
            accuracyInt += 1
        print(round(math.pi, accuracyInt))


def get_console_input_float(requestTextStr):
    while True:
        try:
            return float(input(f'{requestTextStr}: '))
        except ValueError:
            print("You have entered not a float value. Please try again.")


main()

