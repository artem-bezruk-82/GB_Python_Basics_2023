# Семинар 7
# Задание 1
# Создайте пользовательский аналог метода filter().

def main():
    inputList = [1, 2, 3, 4, 5, 6]
    print(inputList)
    outputList1 = list(my_filter(lambda value: value % 2 == 0, inputList))
    print(outputList1)
    outputList2 = list(filter(lambda value: value % 2 == 0, inputList))
    print(outputList2)


def my_filter(function, iterable):
    return (item for item in iterable if function(item))


main()

