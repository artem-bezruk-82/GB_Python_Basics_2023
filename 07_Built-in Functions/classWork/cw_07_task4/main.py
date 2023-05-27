# Семинар 7
# Задача 4.
# Создайте декоратор с параметрами.

def main():
    get_name()


def greetings(helloStr):
    def my_greetings(func):
        def decorator():
            print(f"{helloStr} {func()}")
        return decorator
    return my_greetings


@greetings("Hello")
def get_name():
    return input("What is your name?\n")


main()

