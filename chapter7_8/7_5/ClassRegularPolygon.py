import math

class RegularPolygon:
    
    def __init__(self, n = 3, s = 1.0, x = 0.0, y = 0.0):
        self.__n = n
        self.__s = s
        self.__x = x
        self.__y = y

    def setN(self, n):
        if n < 1:
            print("Negative value entered for number of sides. Unable to process request.")
        else:
            self.__n = n

    def setS(self, s):
        if s < 0:
            print("Negative value enterd for side length. Unable to process request.")
        else:
            self.__s = s

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getN(self):
        return self.__n

    def getS(self):
        return self.__s

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getPerimeter(self):
        perimeter = self.__n * self.__s

        return perimeter

    def getArea(self):
        area = (self.__n * self.__s ** 2) / (4 * math.tan(math.pi / self.__n))
        
        return area

