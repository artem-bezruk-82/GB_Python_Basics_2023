# Семинар 7
# Домашняя работа
# Задание 1
# Создайте пользовательский аналог метода map().


def main():
    inputList = [9, 4, 6, 3, 3, 10, 4]
    print(inputList)
    outputList = list(my_map(lambda value: value * 10, inputList))
    print(outputList)


def my_map(function, iterable):
    return (function(item) for item in iterable)


main()

