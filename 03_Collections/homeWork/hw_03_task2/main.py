# Семинар 3
# Домашняя работа
# Задача 2.
# В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# Список фруктов заполните вручную.


def main():
    firstLetter = get_console_input_char("Please enter 1 letter")
    fruitsList = [
        "Apple",
        "Guava",
        "Lemon",
        "Watermelon",
        "Orange",
        "Peach",
        "Avocado",
        "Pear",
        "Kiwi",
        "Banana",
        "Pineapple"]

    counter = 0
    for fruit in fruitsList:
        if fruit[0].lower() == firstLetter.lower():
            print(fruit)
            counter += 1
    if counter == 0:
        print(f"No fruits started with {firstLetter} letter found")



def get_console_input_char(requestTextStr):
    char = ""
    while True:
        char = str(input(f"{requestTextStr} "))
        if len(char) == 1 and char.isalpha() is True:
            return char
        else:
            if char.isalpha() is False:
                print("You have entered not a letter. Please try again")
            if len(char) != 1:
                print("You need to enter 1 letter. Please try again")


main()
