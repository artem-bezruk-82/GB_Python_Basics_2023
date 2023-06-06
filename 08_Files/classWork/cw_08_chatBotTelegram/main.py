# Семинар 8
# Задача 1. Напишите чат-бота, который записывает сообщения всех пользователей, которые ему написали.
# Задача 2. Добавьте боту возможность регистрации. Добавьте команду, которая запишет id и имя пользователя в файл.
# Задача 3. Добавьте возможность рассылки напоминания всем зарегистрированным пользователям.
# Задача 4. Добавьте боту клавиатуру для основных команд.

import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN", parse_mode=None)

userMessagesFileNameStr = "userMessages.txt"
usersFileNameStr = "users.txt"


def main():
    bot.polling(none_stop=True)


markup = types.ReplyKeyboardMarkup(row_width=2)
registrationBtn = types.KeyboardButton('/registration')
reminderBtn = types.KeyboardButton('/reminder')
markup.add(registrationBtn, reminderBtn)


@bot.message_handler(commands=["start", "registration", "reminder"])
def start(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!")
        bot.send_message(message.chat.id, "выбери действие:", reply_markup=markup)
    elif message.text == "/registration":
        try:
            fileInputStream = open(file=usersFileNameStr, mode='r', encoding="utf-8")
            usersList = fileInputStream.readlines()
            fileInputStream.close()
            usersList = [user.replace('\n', '') for user in usersList]
        except:
            fileInputStream = open(file=usersFileNameStr, mode='w', encoding="utf-8")
            fileInputStream.close()
        if str(message.from_user.id) not in usersList:
            fileOutputStream = open(file=usersFileNameStr, mode='a', encoding="utf-8")
            fileOutputStream.write(f"{message.from_user.id}\n")
            fileOutputStream.close()
            bot.reply_to(message, "Регистрация выполнена")
        else:
            bot.reply_to(message, "Вы уже зарегистрированы")
    elif message.text == "/reminder":
        fileInputStream = open(file=usersFileNameStr, mode='r', encoding="utf-8")
        usersList = fileInputStream.read().split('\n')
        fileInputStream.close()
        for user in usersList:
            if len(user) > 0:
                bot.send_message(user, "test reminder")



@bot.message_handler(content_types=["text"])
def record_message_to_file(message):
    fileOutputStream = open(file=userMessagesFileNameStr, mode='a', encoding="utf-8")
    messageTextStr = f"\n{message.from_user.first_name} {message.from_user.last_name} ({message.from_user.username})" \
                     f"\n{message.text}"
    fileOutputStream.write(messageTextStr)
    fileOutputStream.close()


main()
