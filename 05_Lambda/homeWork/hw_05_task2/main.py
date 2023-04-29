# Семинар 5
# Домашнее задание
# Задача 2
# Дан список случайных чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.
import random


def main():
    valuesList = [random.randint(1, 10) for _ in range(0, 15)]
    print(valuesList)
    increasingList = list()
    increasingList.append(valuesList[0])
    for i in range(1, len(valuesList)):
        if valuesList[i] > increasingList[len(increasingList) - 1]:
            increasingList.append(valuesList[i])
    print(increasingList)


main()
