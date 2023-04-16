# Семинар 2
# Домашняя работа
# Задание 4
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
import random


def main():
    n = 10
    numbers = list()
    for i in range(0, n):
        numbers.append(random.randint(-n, n))

    print("Initial list: ")
    print(numbers)
    cyclic_shift_list(lst=numbers, shiftStepsInt=2)
    print("List: after cyclic shift")
    print(numbers)


def cyclic_shift_list(lst, shiftStepsInt):
    if shiftStepsInt < 0:
        steps = abs(shiftStepsInt)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(shiftStepsInt):
            lst.insert(0, lst.pop())


main()
