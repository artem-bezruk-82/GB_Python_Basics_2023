def main():
    value = get_console_input_int("Please enter integer value")
    print(f"{value} ^ 2 = {value * value}")


def get_console_input_int(requestText):
    while True:
        try:
            return int(input(f"{requestText}: "))
        except ValueError:
            print("You have entered not an integer value. Please try again.")


main()
