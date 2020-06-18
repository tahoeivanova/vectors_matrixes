import numpy as np

# Даны две точки плоскости A(2,3) и B(-3,1). Найти координаты вектора AB
# AB = (x2-x1, y2-y1)
print(f"Vector's Coordinates: {(-3) - 2}, {1-3}")

# Даны две точки плоскости A(1,3) и B(-3,-1). Найти модуль вектора AB
# AB = sqrt(x**2 + y**2)
print(f"Vector's Coordinates: {(-3) - 1}, {(-1) -3}")
print(f"Vector's module: {np.sqrt(((-3) - 1)**2 + ((-1) -3)**2)})")

# Даны два вектора a(1,-3) и b(3,2). Найти: 2a, a+b, a-b
# умножение вектора на число
# C * a(x,y) = b(C*x, C*y)
# сумма вектора a и b - это сумма их координат
# a(x1,y1) + b(x1,y1) = c(x1+x2, y1+y2)
# a(x1,y1) - b(x1,y1) = c(x1-x2, y1-y2)

class vector_2d:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    # умножение вектора на число
    # скаляр - это любое действительное число
    def scalar_multipliers(self, scalar):
        return (self.x * scalar, self.y * scalar)

    # сложение, умножение
    # принимает на вход вектор(объект класса vector_2d и тип операции)
    def add_substract(self, v, type='add'):
        if type == 'add':
            return (self.x+v.x, self.y+v.y)
        if type == 'sub':
            return (self.x - v.x, self.y - v.y)

a = vector_2d((1,-3),)
b = vector_2d((3,2),)

print(f"a Coordinates: {a.x}, {a.y}")
print(f"b Coordinates: {b.x}, {b.y}")
print(f"2*a: {a.scalar_multipliers(2)}")
print(f"a + b: {a.add_substract(b,type='add')}")
print(f"a - b: {a.add_substract(b,type='sub')}")

# Найти скалярное произведение векторов a(1,4) и b(-3,2) , если угол между a и b = pi/6
# a*b = |a|*|b|*cos(a,b)

class vectors_dot_product(vector_2d):
    # add more functions
    def get_module(self):
        return np.sqrt(self.x**2 +self.y**2)

    # функция для вычисления косинуса
    @staticmethod
    def compute_cosine(rad):
        return np.cos(rad)

    # функция вычисления скалярного произведения между двумя векторами
    # на вкод - другой вектор и радианы
    def vector_product(self, v, rad):
        return (self.get_module() * v.get_module()*self.compute_cosine(rad))

a = vectors_dot_product((1,4))
b = vectors_dot_product((-3,2))

print(f'Скалярное произведение a и b: {a.vector_product(b, np.pi/6)}')

# нахождение угла
# cos(a,b) = a*b/(|a|*|b|)
# угол = arccos(a*b/|a|*|b|)
a = vectors_dot_product((1,4))
b = vectors_dot_product((-3,2))
a_b = a.vector_product(b, np.pi/6)
ang = a_b/(a.get_module()*b.get_module())
print(f"Угол равен = {np.arccos(ang)}")

# Скалярное произведение векторов в координатах
# Даны два вектора с координатами (x,y)
# a(x1,y1) * b(x1,y1)= ab(x1*x2 + y1*y2)
print(f'Скалярное произведение ab в координатах: {a.x*b.x + a.y*b.y}')