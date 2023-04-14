# Семинар 1
# Задание 2
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from Point import Point


def main():
    pointX = Point(xFloat=1, yFloat=2, nameStr="X")
    pointY = Point(xFloat=5, yFloat=15, nameStr="Y")
    print(pointX.to_string())
    print(pointY.to_string())

    try:
        print(f"Distance = {round(Point.get_distance(pointX, pointY),2)}")
    except Exception as exc:
        print(exc)


main()
