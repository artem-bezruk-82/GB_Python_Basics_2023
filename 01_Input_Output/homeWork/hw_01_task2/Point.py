class Point:

    defaultNameStr = "Undefined"

    def __init__(self, xFloat, yFloat, nameStr=defaultNameStr):
        if nameStr:
            self.__name = nameStr
        else:
            self.__name = Point.defaultNameStr
        try:
            self.__x = float(xFloat)
            self.__y = float(yFloat)
        except Exception as exc:
            raise exc

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, xFloat):
        try:
            self.__x = float(xFloat)
        except Exception as exc:
            raise exc

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, yFloat):
        try:
            self.__y = float(yFloat)
        except Exception as exc:
            raise exc

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nameStr):
        self.__name = nameStr

    @staticmethod
    def get_distance(pointA, pointB):
        if type(pointA) is Point and type(pointB) is Point:
            return pow(pow((pointB.x - pointA.x), 2) + pow((pointB.y - pointA.y), 2), 0.5)
        else:
            raise Exception("Invalid argument type. The only Point type supported")

    def to_string(self):
        return f"{self.__name}: ({self.__x}; {self.__y})"
