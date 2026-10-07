import math

class tri:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("сторона не может быть меньше или равна 0")
        if (a >= b + c) or (b >= a + c) or (c >= a + b):
            raise ValueError("треугольника с такими сторонами не существует")
        
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def P(self):
        return self.__a + self.__b + self.__c
    
    @property
    def S(self):
        p = self.P / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

    def angles(self):
        cos_a = (self.__b**2 + self.__c**2 - self.__a**2) / (2 * self.__b * self.__c)
        cos_b = (self.__c**2 + self.__a**2 - self.__b**2) / (2 * self.__c * self.__a)
        cos_c = (self.__a**2 + self.__b**2 - self.__c**2) / (2 * self.__a * self.__b)
        
        angleA = math.degrees(math.acos(cos_a))
        angleB = math.degrees(math.acos(cos_b))
        angleC = math.degrees(math.acos(cos_c))
        
        return round(angleA, 1), round(angleB, 1), round(angleC, 1)

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

try:
    t = tri(a, b, c)
    print('NICE')
    print('P:', t.P)
    print('S:', round(t.S, 2))
    
    ang = t.angles()
    print('Углы:', ang[0], ang[1], ang[2])

except ValueError as error:
    print('невозможно создать')
    print('причина:', error)
