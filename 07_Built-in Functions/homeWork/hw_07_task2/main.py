# Семинар 7
# Домашняя работа
# Задача 2
# Создайте декоратор, повторяющий функцию заданное количество раз.


def main():
    my_function()


def repeat_func(numberOfTimesInt):
    def function_handler(func):
        def decorator():
            for i in range(0, numberOfTimesInt):
                print(func() + f" {i + 1} time")
        return decorator
    return function_handler


@repeat_func(5)
def my_function():
    return "My function called"


main()
