# Семинар 8
# Домашняя работа
# Задача 2
# Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.

import json
import telebot

requestsFilePathStr = "requests.txt"

bot = telebot.TeleBot("TOKEN", parse_mode=None)


def main():
    requestsList = get_json_string_format_file_lst(requestsFilePathStr)
    for requestItem in requestsList:
        print(requestItem["request"])
        if len(requestItem["response"]) == 0:
            requestTextStr = requestItem["request"]["text"]
            print(requestItem["request"]["from"]["first_name"] + requestItem["request"]["from"]["last_name"] +
                  "\nRequest text: " + requestTextStr)
            responseTextStr = input("Please enter answer")
            if len(responseTextStr) > 0:
                requestItem["response"] = responseTextStr
                bot.send_message(requestItem["request"]["chat"]["id"],
                                 f"Your request: {requestTextStr} \nOur response: {responseTextStr}")


def get_json_string_format_file_lst(filePath):
    try:
        fileInputStream = open(file=filePath, mode='r', encoding="utf-8")
        recordsList = fileInputStream.read().split('\n')
        fileInputStream.close()
    except:
        fileInputStream = open(file=filePath, mode='w', encoding="utf-8")
        fileInputStream.close()
    objectsList = list()
    for record in recordsList:
        if len(record) > 0:
            objectsList.append(json.loads(record))
    return objectsList


main()
