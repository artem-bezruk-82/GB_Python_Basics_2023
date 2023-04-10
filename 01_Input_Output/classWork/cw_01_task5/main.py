# Семинар 1
# Задание 5 Напишите программу, которая находит наибольшее и наименьшее число из списка значений


def main():
    numbers = [-2, 5, 8, -4, 9, 18, -8]
    maxValue = numbers[0]
    minValue = numbers[0]

    for number in numbers:
        print(number, end=' ')
        if number > maxValue:
            maxValue = number
        if number < minValue:
            minValue = number

    print(f"\nMax value: {maxValue}; Min value:{minValue}")


main()
