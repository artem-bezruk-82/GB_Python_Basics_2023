# Семинар 5
# Задание 0
# Заполните список случайным образом числами от 1 до 100.
# С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5.
import random


def main():
    numbersList = [random.randint(1, 100) for _ in range(0, 15)]
    print(numbersList)
    numbersList = list(filter(lambda n: n % 5 == 0, numbersList))
    print(numbersList)


main()

