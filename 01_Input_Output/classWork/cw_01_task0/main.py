
def get_console_input_int(request_text):
    while True:
        try:
            return int(input(f"{request_text}: "))
        except ValueError:
            print("You have entered not an integer value. Please try again: ")


value = get_console_input_int("Please enter integer value")
print(f"{value} ^ 2 = {value*value}")
