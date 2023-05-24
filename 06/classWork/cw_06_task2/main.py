# Семинар 6
# Задание 2
# Даны два случайных пятизначных числа. Определить, состоят ли они из одних и тех же цифр.
import random


def main():
    value1 = random.randint(10000, 99999)
    value2 = random.randint(10000, 99999)

    print("variant #1")
    print(f"{value1} and {value2} consist of" + (" the same " if is_same_digits_1(value1, value2) else " different ") +
          "set of digits")

    print("variant #2")
    print(f"{value1} and {value2} consist of" + (" the same " if is_same_digits_2(value1, value2) else " different ") +
          "set of digits")


def is_same_digits_1(value1, value2):
    value1List = list(str(value1))
    value2List = list(str(value2))
    value1List.sort()
    value2List.sort()
    value1SortedStr = str().join(value1List)
    value2SortedStr = str().join(value2List)
    return True if value1SortedStr == value2SortedStr else False


def is_same_digits_2(value1, value2):
    value1Str = str(value1)
    value2Str = str(value2)
    digits1Lst = [int(i) for i in value1Str]
    digits2Lst = [int(i) for i in value2Str]
    digits1Lst.sort()
    digits2Lst.sort()
    return True if digits1Lst == digits2Lst else False


main()

