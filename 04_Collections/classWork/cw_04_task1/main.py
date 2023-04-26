# Семинар 4
# Задание 1
# Создайте кортеж, заполненный случайными числами.
# Напишите метод, который заменяет элемент в кортеже по заданному индексу другим случайным числом.
import random


def main():
    myTuple = tuple(random.randint(0, 100) for _ in range(0, 10))
    print(f"Initial tuple:\n{myTuple}")
    index = random.randint(0, len(myTuple))
    print(f"change element {index} with random value")
    try:
        myTuple = replace_tuple_element_random(myTuple, index)
        print(f"Final tuple:\n{myTuple}")
        myTuple = change_tuple_element_random(myTuple, index)
        print(f"Final tuple:\n{myTuple}")
    except Exception as exc:
        print(exc)


def replace_tuple_element_random(tpl, indexInt):
    if indexInt >= len(tpl) or indexInt < 0:
        raise IndexError(f"Index is out of 0...{len(tpl) - 1} range.")
    tempList = list(tpl[:indexInt])
    tempList.append(random.randint(0, 100))
    tempList.extend(tpl[indexInt + 1:])
    return tuple(tempList)


def change_tuple_element_random(tpl, indexInt):
    if indexInt >= len(tpl) or indexInt < 0:
        raise IndexError(f"Index is out of 0...{len(tpl) - 1} range.")
    return tpl[:indexInt] + (random.randint(0, 100),) + tpl[indexInt + 1:]


main()
