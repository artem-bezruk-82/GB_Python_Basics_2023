# Семинар 3
# Задание 4
# Ручка стоит – 5 рублей, карандаш – 3 рубля, ластик – 4 рубля.
# Кассир последовательно вводит в программу позиции из чека «ручка», «карандаш», «ластик».
# Ввод заканчивается, когда введено слово «стоп».
# Определите сумму чека.


def main():
    stationeryDict = {
        "pen": 5,
        "pencil": 3,
        "eraser": 4
    }

    total = 0
    flagBool = True

    while flagBool:
        item = str(input("Please enter stationery [pen, pencil, eraser] or [stop] to end program: "))
        if item.lower() == "stop":
            flagBool = False
        elif item in stationeryDict:
            total += stationeryDict[item]
        else:
            print(f"There is no [{item}] item it the stationery collection")
    print(total)


main()
