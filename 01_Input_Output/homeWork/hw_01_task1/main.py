def main():
    dayNumberInt = get_console_input_int("Enter a day number from 1 to 7: ")
    try:
        print(get_week_day_name_string(dayNumberInt))
    except Exception as exc:
        print(exc)


def get_week_day_name_string(dayNumberInt):
    match dayNumberInt:

        case 1:
            return "Monday"

        case 2:
            return "Tuesday"

        case 3:
            return "Wednesday"

        case 4:
            return "Thursday"

        case 5:
            return "Friday"

        case 6:
            return "Saturday"

        case 7:
            return "Sunday"

        case _:
            raise Exception("number is out of 1..7 range")


def get_console_input_int(requestTextStr):
    while True:
        try:
            return int(input(f'{requestTextStr}: '))
        except ValueError:
            print("You have entered not a =n integer value. Please try again.")


main()
