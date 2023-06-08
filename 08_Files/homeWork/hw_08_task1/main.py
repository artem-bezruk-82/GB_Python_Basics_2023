# Семинар 8
# Домашняя работа
# Задача 1
# Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot
from telebot import types
import json


bot = telebot.TeleBot("TOKEN", parse_mode=None)

filePath = "requests.txt"


def main():
    bot.polling(none_stop=True)


@bot.message_handler(commands=["start"])
def start(message):
    if message.from_user.is_bot == False:
        bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}!")
        bot.send_message(message.chat.id, f"/request to raise your request")


@bot.message_handler(content_types=["text"])
def menu(message):
    if message.text == "/request":
        msg = bot.send_message(message.chat.id, "Please enter your request text")
        bot.register_next_step_handler(msg, record_message_to_file)


@bot.message_handler(content_types=["text"])
def record_message_to_file(message):
    requestDic = {
        "request": message.json,
        "response": ""
    }
    fileOutputStream = open(file=filePath, mode='a')
    fileOutputStream.write(f"{json.dumps(requestDic)}\n")
    fileOutputStream.close()
    msg = bot.send_message(message.chat.id, "Thank your for your request. We will come back to you with solution soon!")
    bot.register_next_step_handler(msg, start)


main()
