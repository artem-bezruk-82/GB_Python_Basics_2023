# Семинар 6
# Задача 3
# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

def main():
    expression = " 9  / 3 "
    print(get_operation(expression))




def get_operation(expressionStr):
    expressionStr = expressionStr.replace(" ", "")
    expressionStr = expressionStr.replace("-", "+-")
    expressionStr = expressionStr.replace("/", "*1/")
    if '+' in expressionStr:
        a, b = map(int, expressionStr.split('+'))
        return a + b
    #elif '-' in expressionStr:
    #    a, b = map(int, expressionStr.split('-'))
    #    return a - b
    elif '*' in expressionStr:
        a, b = map(float, expressionStr.split('-'))
        return a * b
    #elif '/' in expressionStr:
    #    a, b = map(float, expressionStr.split('-'))
    #    return a / b
    else:
        return int(expressionStr)


main()

