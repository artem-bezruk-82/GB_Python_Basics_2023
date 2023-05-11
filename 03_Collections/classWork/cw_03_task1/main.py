# Семинар 3
# Задание 1
# В списке хранятся сведения о количестве осадков, выпавших за каждый день июня.
# Определите в какой период выпало больше осадков: в первой или второй половине июня.
# Примечание: список заполняется случайными числами от 0 до 25.
import random


def main():
    precipitation = [random.randint(0, 25) for index in range(0, 30)]

    print(precipitation)
    if sum(precipitation[:len(precipitation)//2]) == sum(precipitation[len(precipitation)//2:]):
        print("First and second half of June had tha same precipitation volume")
    else:
        print("First half of June had " +
              ("more" if sum(precipitation[:len(precipitation)//2]) > sum(precipitation[len(precipitation)//2:]) else "less")
              +
              " precipitation than second one")


main()
