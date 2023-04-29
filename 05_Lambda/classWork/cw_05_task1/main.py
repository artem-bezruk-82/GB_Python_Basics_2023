# Семинар 5 Задание 1
# На вход подаётся четырёхзначное число. Получите список, состоящий из цифр данного числа, увеличенных на 10.
import random


def main():
    valueInt = random.randint(1000, 10000)
    print(valueInt)
    valuesList = list()
    while valueInt > 1:
        valuesList.append((valueInt % 10)+10)
        valueInt = int(valueInt / 10)
    print(valuesList)


main()
