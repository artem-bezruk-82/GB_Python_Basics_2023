# Семинар 5
# Задание 2
# В зоопарк отправили отчёт о новом поступлении зверей с ошибкой, в результате которой некоторые данные не расшифровались.
# Расшифруйте данные.
# Определите, в какой клетке находится лев. Номер клетки совпадает с номером строки.


def main():
    encryptedAnimalsList = [
        "001101000101000100000010000101000100011101",
        "000010001111001100001011",
        "001100000101000010",
        "001011010001001111001100001001001011",
    ]

    encryptedAnimalLength = 6

    alphabetStr = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    print(alphabetStr)
    alphabetDict = dict()
    for i in range(0, len(alphabetStr)):
        alphabetDict[int_to_binary_str(i, encryptedAnimalLength)] = alphabetStr[i]
    print(alphabetDict)

    decryptedAnimalList = list()
    for animalEncrypted in encryptedAnimalsList:
        position = 0
        animalDecryptedStr = str()
        while position < len(animalEncrypted):
            animalDecryptedStr += alphabetDict.get(animalEncrypted[position:(position + encryptedAnimalLength)], '*')
            position += encryptedAnimalLength
        decryptedAnimalList.append(animalDecryptedStr)
    print(decryptedAnimalList)

    cageInt = -1
    animalStr = "Лев"
    for i in range(0, len(decryptedAnimalList) - 1):
        if decryptedAnimalList[i] == animalStr.lower():
            cageInt = i
            break
    print(f"{animalStr} is in cage {cageInt}" if cageInt >= 0 else f"there is no {animalStr} in the list")


def int_to_binary_str(valueInt, numberOfDigits = 0):
    valueInt = abs(int(valueInt))
    binaryStr = str()
    while valueInt > 0:
        binaryStr = str(valueInt % 2) + binaryStr
        valueInt //= 2
    while len(binaryStr) < numberOfDigits:
        binaryStr = '0' + binaryStr
    return binaryStr


main()

