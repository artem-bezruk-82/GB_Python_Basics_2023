# Семинар 5
# Домашняя работа
# Задание 1
# Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
import random


def main():
    numbersList = [random.randint(1, 10) for _ in range(1, 15)]
    print(numbersList)
    numbersList = list(filter(lambda number: number > 5, numbersList))
    print(numbersList)


main()

