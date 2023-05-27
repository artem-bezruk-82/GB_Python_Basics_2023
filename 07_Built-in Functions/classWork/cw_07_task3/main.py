#  Семинар 7
#  Задача 3
#  Создайте декоратор для метода нахождения суммы.

def main():
    my_sum(3, 5, 2, 1)


def my_format(function):
    def decorator(*args):
        print(f"sum{args} = {function(*args)}")
    return decorator


@my_format
def my_sum(a, b, c, d):
    return a + b + c + d


main()

