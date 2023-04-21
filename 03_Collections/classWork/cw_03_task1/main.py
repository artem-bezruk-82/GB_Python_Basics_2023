# Семинар 3
# Задание 1
# В списке хранятся сведения о количестве осадков, выпавших за каждый день июня.
# Определите в какой период выпало больше осадков: в первой или второй половине июня.
# Примечание: список заполняется случайными числами от 0 до 25.
import random


def main():
    junePrecipitation = list()
    for i in range(0, 30):
        junePrecipitation.append(random.randint(0, 25))
    print(junePrecipitation)
    if junePrecipitation[:15] == junePrecipitation[15:]:
        print("First and second half of June had tha same precipitation volume")
    else:
        print("First half of June had " + ("more" if junePrecipitation[:15] > junePrecipitation[15:] else "less") +
              " precipitation than second one")


main()
