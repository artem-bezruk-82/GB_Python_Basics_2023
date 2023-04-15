# Семинар 2
# Домашняя работа
# Задание 3
# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй

def main():
    firstStr = "one"
    secondStr = "onetwonine"
    for i in range(0, len(firstStr)):
        counter = 0
        for j in range(0, len(secondStr)):
            if firstStr[i] == secondStr[j]:
                counter += 1
        print(f"{firstStr[i]} - {counter}")


main()
