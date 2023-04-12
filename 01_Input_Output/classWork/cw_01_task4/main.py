# Семинар 1
# Задача 4
# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

def main():
    value = abs(get_console_input_float("Please enter float value"))
    decimalPart = float(value) - int(value)
    resultStr = str(decimalPart)[2] if decimalPart != 0 else "No decimal part"
    print(resultStr)


def get_console_input_float(requestTextStr):
    while True:
        try:
            return float(input(f"{requestTextStr}: "))
        except ValueError:
            print("You have entered not a float value. Please try again")


main()
