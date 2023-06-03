# Семинар 8
# Задача 1. Напишите чат-бота, который записывает сообщения всех пользователей, которые ему написали.

import telebot
from telebot import types

bot = telebot.TeleBot("5869173866:AAHZhIrRRM9idhfFugSDw6wQQS5ALHbioZ0", parse_mode=None)


def main():
    bot.polling(none_stop=True)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!")


main()
