# Семинар 3 Задние 2
# Напишите программу, которая позволит пользователю заполнить анкету, последовательно вводя в программу:
# - имя; - возраст; - хобби; - любимое животное.
# После окончания ввода, выводится заполненная анкета.


def main():
    print("*** variant #1 with tuple***")
    print("Hi, please fill in our short questionary form")
    questionnaireTuple = get_questionnaire_console_tuple()
    questionnaire_tuple_print_console(*questionnaireTuple)

    print("*** variant #2 with dictionary ***")
    print("Hi, please fill in our short questionary form")
    questionnaireDic = get_questionnaire_console_dict()
    for key in questionnaireDic:
        print(f"{key}: {questionnaireDic[key]}", end=' ')


def get_questionnaire_console_dict():
    questionnaireDict = dict()
    questionnaireDict["name"] = str(input("Please enter your name: "))
    questionnaireDict["age"] = abs(get_console_input_int("Please enter your age: "))
    questionnaireDict["hobby"] = str(input("Please enter your hobby: "))
    questionnaireDict["animal"] = str(input("Please enter your favourite animal: "))
    return questionnaireDict


def get_questionnaire_console_tuple():
    name = str(input("Please enter your name: "))
    age = abs(get_console_input_int("Please enter your age: "))
    hobby = str(input("Please enter your hobby: "))
    animal = str(input("Please enter your favourite animal: "))
    return name, age, hobby, animal


def questionnaire_tuple_print_console(name, age, hobby="not defined", animal="not defined"):
    print(f"Name: {name}; Age: {age}; Hobby: {hobby}; Favourite Animal: {animal}")


def get_console_input_int(requestTextStr):
    while True:
        try:
            return int(input(f'{requestTextStr}: '))
        except ValueError:
            print("You have entered not a =n integer value. Please try again.")


main()
