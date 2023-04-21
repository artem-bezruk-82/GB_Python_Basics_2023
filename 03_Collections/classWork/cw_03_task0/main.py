# Семинар 3
# Задание 0
# Дан список, заполненный случайными числами от 0 до 10. Определите, является ли сумма всех элементов чётной.
import random


def main():
    numbers = list()
    for i in range(0, 10):
        numbers.append(random.randint(0, 10))
    print(numbers)
    sumInt = sum(numbers)
    print(str(sumInt) + " is " + ("even" if sumInt % 2 == 0 else "odd"))


main()
