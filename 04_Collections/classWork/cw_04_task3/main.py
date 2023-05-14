# Семинар 4
# Задание 3
# Сгенерируйте список случайных чисел от 1 до 20, состоящий из 10 элементов.
# Удалите из списка дубликаты уже имеющихся элементов.
# Определите, сколько элементов было удалено.
import random


def main():
    numbersList = [random.randint(1, 20) for _ in range(0, 10)]
    print(numbersList)
    lenInit = len(numbersList)
    numbersList = list(set(numbersList))
    print(numbersList)
    print(f"{lenInit - len(numbersList)} repetitive elements have been deleted")


main()

