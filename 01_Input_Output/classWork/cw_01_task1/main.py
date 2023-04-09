# Семинар 1
# Задача 1
# Напишите программу, которая на вход принимает два числа и проверяет, является ли второе число квадратом первого.

def main():
    firstValue = get_console_input_int("Please enter first value")
    secondValue = get_console_input_int("Please enter second value")
    sign = "=" if secondValue == firstValue * firstValue else "!="
    print(f"{firstValue}^2 {sign} {secondValue}")


def get_console_input_int(requestText):
    while True:
        try:
            return int(input(f"{requestText}: "))
        except ValueError:
            print("You have entered not an integer value. Please try again.")


main()
