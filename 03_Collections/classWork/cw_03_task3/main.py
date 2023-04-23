# Семинар 3
# Задача 3
# Напишите скрипт генератора паролей заданной длины, состоящих из латинских букв и чисел.
import random


def main():
    lettersStr = "qwertyuiopasdfghjklzxcvbnm"
    passwordLength = random.randint(8, 17)
    passwordStr = ""

    while len(passwordStr) < passwordLength:
        randomValue = random.randint(0, len(lettersStr) - 1)
        passwordStr += lettersStr[randomValue]
        if randomValue % 2 == 0:
            passwordStr += str(random.randint(0, 9))

    print(f"Password: {passwordStr}")


main()
