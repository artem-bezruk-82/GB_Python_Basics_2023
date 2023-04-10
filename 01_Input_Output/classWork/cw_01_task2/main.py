# Семинар 1
# Задание 2 Организуйте последовательный ввод чисел до тех ор, пока не будет введён 0.
# Подсчитайте среди введённых чисел те, которые кратны трём.

def main():
    counter = 0
    value = get_console_input_int("Please enter value")
    while value != 0:
        value = get_console_input_int("Please enter value")
        if value % 3 == 0 and value != 0:
            counter += 1
    print(f"There ware {counter} times multiples of 3 met")


def get_console_input_int(requestTextStr):
    try:
        return int(input(f'{requestTextStr}: '))
    except ValueError:
        print("You have entered not an integer value. Please try again.")


main()
