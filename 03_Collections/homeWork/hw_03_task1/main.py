#  Семинар 1
#  Занатие 1
#  Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.

def main():
    print(get_fibonacci_list(get_console_input_int("Please enter integer value")))


def get_fibonacci_list(firstElementsInt):
    firstElementsInt = abs(firstElementsInt)
    fibonacciList = [0, 1]
    for i in range(2, firstElementsInt + 1):
        fibonacciList.append(fibonacciList[i - 2] + fibonacciList[i - 1])
    return fibonacciList


def get_console_input_int(requestTextStr):
    while True:
        try:
            return int(input(f'{requestTextStr}: '))
        except ValueError:
            print("You have entered not an integer value. Please try again.")


main()
