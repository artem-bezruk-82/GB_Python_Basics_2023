# Семинар 5
# Задача 1
# Дан список случайных элементов. Проверьте, что все его элементы уникальны.
import random


def main():
    randomNumbersList = [random.randint(0, 9) for _ in range(0, random.randint(3, 15))]
    print(randomNumbersList)
    print("List elements are" + (" " if len(randomNumbersList) == len(set(randomNumbersList)) else " not ") + "unique")


main()

