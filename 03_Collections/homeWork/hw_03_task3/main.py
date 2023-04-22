# Семинар 3
# Домашняя работа
# Задание 3
# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.


def main():

    answersDictionary = {
        "hi": "Hi, nice to see you!",
        "hello": "Hello, nice to see you!",
        "what is your name?": "My name is Bob, and I'm a bot"
    }

    phrase = str(input("Please enter your phrase: ")).lower()
    try:
        print(answersDictionary[phrase])
    except:
        print("Sorry, I do not know what you are talking about")


main()
