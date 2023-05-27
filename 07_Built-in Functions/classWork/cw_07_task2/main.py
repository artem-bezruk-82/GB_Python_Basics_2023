# Семинар 7
# Задача 2
# Создайте метод, позволяющий замерить время работы других методов.
import time


def main():
    our_math_str()
    our_math_int()



def stopwatch(func):
    def decorator():
        startTime = time.time()
        func()
        print(f"Execution time: {time.time() - startTime}")
    return decorator


@stopwatch
def our_math_str():
    numberStr = "123"
    resultInt = int(numberStr) + int(numberStr * 2) + int(numberStr * 3)
    print(resultInt)


@stopwatch
def our_math_int():
    numberInt = 123
    resultInt = numberInt + numberInt*1000 + numberInt + numberInt*1000000 + numberInt*1000 + numberInt
    print(resultInt)


main()
