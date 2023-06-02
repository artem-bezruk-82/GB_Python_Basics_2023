# Семинар 7
# Домашняя работа
# Задача 3.
# Добавьте в telegram-бота игру «Угадай числа».
# Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных ходов.

import telebot
from telebot import types
import requests

bot = telebot.TeleBot("TOKEN", parse_mode=None)


def main():
    bot.polling(none_stop=True)


@bot.message_handler(commands=["start"])
def start(message):
    buttonsMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    weatherButton = types.KeyboardButton("Погода")
    gameButton = types.KeyboardButton("Угадай число")
    buttonsMarkup.add(weatherButton, gameButton)

    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!", reply_markup=buttonsMarkup)


@bot.message_handler(content_types=["text"])
def bot_menu(message):
    messageTextStr = str(message.text).lower()
    if message.chat.type == "private":
        match messageTextStr:
            case "погода":
                get_weather(message)
            case "угадай число":
                guess_value_game(message)



@bot.message_handler(content_types=["text"])
def get_weather(message):
    weatherRequest = requests.get(url="https://wttr.in/?0TQ")
    bot.reply_to(message, weatherRequest.text)


@bot.message_handler(content_types=["text"])
def guess_value_game(message):
    buttonsMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    stopGameButton = types.KeyboardButton("Завершить игру")
    buttonsMarkup.add(stopGameButton)
    global valueInt
    global attemptsCounter
    valueInt = 35
    attemptsCounter = 0
    msg = bot.send_message(message.chat.id, "Введи число от 1 до 1000", reply_markup=buttonsMarkup)
    bot.register_next_step_handler(msg, get_guess_value)


def get_guess_value(message):
    guessValueStr = str(message.text)

    if not guessValueStr.isdigit():
        if guessValueStr == "Завершить игру":
            msg = bot.send_message(message.chat.id, "Пока")
            bot.register_next_step_handler(msg, start)
        else:
            msg = bot.reply_to(message, "Это не число. Введите число")
            bot.register_next_step_handler(msg, get_guess_value)
        return

    guessValueInt = int(guessValueStr)
    global attemptsCounter
    attemptsCounter += 1
    if guessValueInt != valueInt:
        msg = bot.reply_to(message, "Число " + ("больше" if guessValueInt > valueInt else "меньше") + " загаданного")
        bot.register_next_step_handler(msg, get_guess_value)
    else:
        msg = bot.send_message(message.chat.id, f"Ты угадал число с {attemptsCounter} попыток")
        bot.register_next_step_handler(msg, start)
        return


main()
