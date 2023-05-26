# Семинар 4
# Домашняя работа
# Задание 4
# Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.


def main():
    polynomialStrA = "5x^2 + 3x"
    polynomialStrB = "3x^2 - x + 8"
    polynomialListA = get_polynomial_split_lst(polynomialStrA)
    #print(polynomialListA)
    #print(polynomialListA)
    polynomialListB = get_polynomial_split_lst(polynomialStrB)
    #print(polynomialListB)

def get_polynomial_split_lst(polynomialStr):
    polynomialStr = polynomialStr.lower()
    polynomialStr = polynomialStr.replace(' ', '')
    polynomialStr = polynomialStr.replace('-', '+-')
    polynomialList = polynomialStr.split('+')
    for i in range(0, len(polynomialList)):
        if "x^" not in polynomialList[i]:
            if "x" in polynomialList[i]:
                polynomialList[i] = polynomialList[i].replace("x", "x^1")
            else:
                polynomialList[i] += "x^0"
    print(polynomialList)

    #polynomialMap = map(lambda string: int(string) if len(string) > 0 else 1, polynomialList)
    #return list(polynomialMap)


main()

