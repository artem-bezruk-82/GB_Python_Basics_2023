# Семинар 7
# Задача 5
# Создайте telegram-бота, добавьте в него метод приветствия пользователя.

import telebot
import requests

bot = telebot.TeleBot("TOKEN", parse_mode=None)


def main():
    bot.polling()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=['text'])
def greetings(message):
    userTextStr = str(message.text).lower()
    if "привет" in userTextStr:
        bot.reply_to(message, f"Привет, {message.from_user.first_name}")
    elif userTextStr == "погода":
        weatherRequest = requests.get(url="https://wttr.in/?0TQ")
        bot.reply_to(message, weatherRequest.text)
        print(weatherRequest.text)


main()
