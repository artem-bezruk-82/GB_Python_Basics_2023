# Семинар 4
# Задание 0
# Создайте кортеж. Запишите в него 10 случайных чисел.
import random


def main():
    myTuple = tuple(random.randint(0, 100) for _ in range(0, 10))
    print(myTuple)


main()
