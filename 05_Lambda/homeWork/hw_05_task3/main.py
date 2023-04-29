# Семинар 5
# Домашняя работа
# Задание 3
# Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы.
import random


def main():
    numbersList = [random.randint(1, 10) for _ in range(0, 15)]
    print(numbersList)
    repetitiveNumbers = len(numbersList)
    numbersList = list(set(numbersList))
    repetitiveNumbers -= len(numbersList)
    print(f"Repetitive numbers: {repetitiveNumbers}")
    print(numbersList)


main()
