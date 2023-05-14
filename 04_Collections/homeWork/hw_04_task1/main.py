# Семинар 4
# Домашняя работа
# Задание 1
# Дано натуральное число N.
# Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.


def main():
    value = get_console_input_int("Please enter integer value")
    testTuple = get_factors_tuple(value)
    factorsList = testTuple[0]
    numberOfFactorsInt = testTuple[1]
    if numberOfFactorsInt == 0:
        print(f'{value} is simple value')
    else:
        print(f"{value} has {numberOfFactorsInt} factors, that are: {factorsList}")


def get_factors_tuple(valueInteger):
    if type(valueInteger) is not int:
        raise Exception("Argument is not an integer type")
    valueInt = abs(valueInteger)
    factorInt = 2
    factorsList = list()
    while valueInt != 1 and factorInt <= valueInteger//2:
        if valueInt % factorInt == 0:
            factorsList.append(factorInt)
            valueInt /= factorInt
        else:
            factorInt += 1
    return factorsList, len(factorsList)


def get_console_input_int(requestTextStr):
    while True:
        try:
            return int(input(f'{requestTextStr}: '))
        except ValueError:
            print("You have entered not a =n integer value. Please try again.")


main()

