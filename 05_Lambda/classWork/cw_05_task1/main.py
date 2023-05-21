# Семинар 5 Задание 1
# На вход подаётся четырёхзначное число. Получите список, состоящий из цифр данного числа, увеличенных на 10.
import random


def main():
    valueInt = random.randint(1000, 10000)
    print(valueInt)
    print("variant 1")
    digitsList1 = get_digits_list(valueInt, 10)
    print(digitsList1)
    print("variant 2")
    digitsList2 = [int(digit) + 10 for digit in str(valueInt)]
    print(digitsList2)


def get_digits_list(valueInt, increaseInt = 0):
    valueInt = abs(int(valueInt))
    digits = list()
    while valueInt >= 1:
        digits.append(valueInt % 10)
        valueInt = int(valueInt / 10)
    digits = list(map(lambda digit: digit + abs(int(increaseInt)), digits))
    return list(reversed(digits))


main()
