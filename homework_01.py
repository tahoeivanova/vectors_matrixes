import numpy as np

'''
Задачи Лайт:

Задача 1 а) Даны точки A(-2,5) и B(1,7) . Найти векторы AB и BA. б) Даны точки A(-1,-1) , B(1,1) и C(0,2). Найти векторы AB, AC и BC. в) Даны точки A(-1,3,1) и B(3,2,7) . Найти векторы AB и BA.

Задача 2 Дано: A(-2,5) и B(1,7) Найти модуль вектора AB

Задача 3 Даны векторы a(1,4,-5) и b(2,-5,3) найти 3a-2b, -a + 4b

Задача 4 Даны векторы a(0,2,-1) и b(1,-4,2)и c(0,3,0) найти 3a-5b+0,5c

Задача 6 Найти скалярное произведение векторов a(2,4) и b(0,-1) , если угол между a и b = pi/2

Задача 7 Найти угол между векторами a и b, если известно, что |a| = 4 и |b| = 2* np.sqrt(2), a*b = 8

Задача 8 Какой знак будет у скалярного произведения a и b, если известно что угол(a,b) равен: а) pi/3 б)pi

Задача 9 Даны матрицы k = [[2,-3],[4,-6]] и l = [[9,-6],[6,-4]] вычислить: a) 3k, b) 1/2*l c) k-l d) l+k
'''

# Задача 1 а) Даны точки A(-2,5) и B(1,7). Найти векторы AB и BA.
# б) Даны точки A(-1,-1) , B(1,1) и C(0,2). Найти векторы AB, AC и BC.
# в) Даны точки A(-1,3,1) и B(3,2,7) . Найти векторы AB и BA.

class Coord2d:

    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
    def calculate_vector(self, other):
        return (other.x - self.x), (other.y - self.y)

A = Coord2d(coords=(-2, 5))
B = Coord2d(coords=(1, 7))
print('Задача 1\nа) Даны точки A(-2,5) и B(1,7). Найти векторы AB и BA.')
# в) Даны точки A(-1,3,1) и B(3,2,7) . Найти векторы AB и BA.')
print(f'Вектор AB: {A.calculate_vector(B)}')
print(f'Вектор BA: {B.calculate_vector(A)}')
print('б) Даны точки A(-1,-1) , B(1,1) и C(0,2). Найти векторы AB, AC и BC.')
A = Coord2d(coords=(-1,-1))
B = Coord2d(coords=(1, 1))
C = Coord2d(coords=(0,2))
print(f'Вектор AB: {A.calculate_vector(B)}')
print(f'Вектор AC: {A.calculate_vector(C)}')
print(f'Вектор BC: {B.calculate_vector(C)}')

print('в) Даны точки A(-1,3,1) и B(3,2,7). Найти векторы AB и BA.')

class Coord3d:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]

    def calculate_vector(self, other):
        return (other.x - self.x), (other.y - self.y),  (other.z - self.z)

A = Coord3d(coords=(-1,3,1))
B = Coord3d(coords=(3,2,7))
print(f'Вектор AB: {A.calculate_vector(B)}')
print(f'Вектор BA: {B.calculate_vector(A)}')

print('Задача 2\nДано: A(-2,5) и B(1,7) Найти модуль вектора AB')

class VectorModule(Coord2d):
    def __init__(self, coords):
        super().__init__(coords)
    def calculate_module(self):
        return np.sqrt(self.x**2 + self.y**2)
A = VectorModule(coords=(-2,5))
B = VectorModule(coords=(1,7))

vector_coord = A.calculate_vector(B)
print(f'Координаты вектора AB: {vector_coord}')
v_module = VectorModule(coords=vector_coord)
print(f'Модуль вектора AB: {v_module.calculate_module()}')

print('Задача 3\nДаны векторы a(1,4,-5) и b(2,-5,3). Найти 3a-2b, -a + 4b')
class Vector3d(Coord3d):
    def __init__(self, coords):
        super().__init__(coords)

    def mult_scalar(self, scalar):
        return self.x*scalar, self.y*scalar, self.z*scalar
    @staticmethod
    def add_sub(v1,v2, type='add'):
        if type == 'add':
            x = v1[0] + v2[0]
            y = v1[1] + v2[1]
            z = v1[2] + v2[2]
        if type == 'sub':
            x = v1[0] - v2[0]
            y = v1[1] - v2[1]
            z = v1[2] - v2[2]

        return x, y, z


a = Vector3d(coords=(1,4,-5))
b = Vector3d(coords=(2,-5,3))
print(f'3a: {a.mult_scalar(3)}')
print(f'2b: {b.mult_scalar(2)}')
print(f'3a-2b: {Vector3d.add_sub(a.mult_scalar(3), (b.mult_scalar(2)), type="sub")}')
print(f'-a: {a.mult_scalar(-1)}')
print(f'4b: {b.mult_scalar(4)}')
print(f'-a + 4b: {Vector3d.add_sub(*(a.mult_scalar(-1), b.mult_scalar(4)), type="add")}')

print('Задача 4\nДаны векторы a(0,2,-1) и b(1,-4,2)и c(0,3,0) найти 3a-5b+0,5c')
a = Vector3d(coords=(0,2,-1))
b = Vector3d(coords=(1,-4,2))
c = Vector3d(coords=(0,3,0))

print(f'3a-5b+0,5c: {Vector3d.add_sub(Vector3d.add_sub(a.mult_scalar(3), b.mult_scalar(-5)), c.mult_scalar(0.5))}')

print('Задача 6\nНайти скалярное произведение векторов a(2,4) и b(0,-1), если угол между a и b = pi/2')

class VectorDotProd(VectorModule):
    def __init__(self, coords):
        super().__init__(coords)

    def dot_prod(self, other, rad):
        return np.sqrt(self.x**2 + self.y**2) * np.sqrt(other.x**2 + other.y**2) * np.cos(rad)

# a(2,4) и b(0,-1), если угол между a и b = pi/2'
a = VectorDotProd(coords=(2,4))
a = VectorDotProd(coords=(0,-1))
# pi/2 - 90 градусов, значит скалярное произведение равно 0
print(f'Скалярное произведение: {round(a.dot_prod(b, rad=np.pi/2),15)}')

print('Задача 7\nНайти угол между векторами a и b, если известно, что |a| = 4 и |b| = 2* np.sqrt(2), a*b = 8')
# angle = np.arccos((a*b)/(|a|*|b|))
angle = np.arccos((8)/(4*2*np.sqrt(2)))
print(f'Угол равен {angle}')

print('Задача 8\nКакой знак будет у скалярного произведения a и b, если известно что угол(a,b) равен: а) pi/3 б)pi')
print('От 0 до 90 градусов - скалярное произведение положительное')
print('От 90 до 180 градусов - скалярное произведение отрицательно')
print('90 градусов - скалярное произведение равно 0')
print('а) pi/3 = 60 градусов, скалярное произведение положительное')
print('а) pi = 180 градусов, скалярное произведение отрицательное')


print('Задача 9\nДаны матрицы k = [[2,-3],[4,-6]] и l = [[9,-6],[6,-4]]\nвычислить:\
\na) 3k, b) 1/2*l c) k-l d) l+k')
k = np.array([[2,-3],[4,-6]])
l = np.array([[9,-6],[6,-4]])

class Matrix:
    def __init__(self, *args):
        self.matrix = args[0]
    def __str__(self):
        return f'{self.matrix}'

    def prod_matrix(self, scalar):
        output_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                new_value = self.matrix[i][j] * scalar
                row.append(new_value)
            output_matrix.append(row)
        return np.array(output_matrix)

    def add_sub_matrix(self, other, type='add'):
        output_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                if type == 'add':
                    new_value = self.matrix[i][j] + other.matrix[i][j]
                if type == 'sub':
                    new_value = self.matrix[i][j] - other.matrix[i][j]
                row.append(new_value)
            output_matrix.append(row)
        return np.array(output_matrix)


k_matrix = Matrix(k)
l_matrix = Matrix(l)

print(f'Матрица k:\n{k_matrix}')
print(f'Матрица l:\n{l_matrix}')

print(f'3k: \n{k_matrix.prod_matrix(3)}')
print(f'1/2*l: \n{l_matrix.prod_matrix(0.5)}')
print(f'k-l: \n{k_matrix.add_sub_matrix(l_matrix, type="sub")}')
print(f'l+k: \n{l_matrix.add_sub_matrix(k_matrix)}')

# PRO
#
# print('Задача 1\nНайти скалярное произведение векторов с=-2a+b и d=a-b, если известно что: \
# a и b - вектора, |a| = 4 * np.sqrt(2) и |b| = 8, угол(a,b) = pi/4')
# # cos(a,b) = ((-2a+b) * (a-b))/|(-2a+b)|*|(a-b)|
# # |a| = np.sqrt(x**2 + y**2)
# print('Задача 2\nНайти модуль векторов с=—a+3b , если известно что:\
# a и b - вектора, |a| = 3 и |b| = 2, угол(a,b) = pi/3')

print('Задача 4\nДаны матрицы k = [[5,8,-4],[6,9,-5],[4,7,-3]] и l = [[3,2,5],[4,-1,3],[9,6,5]]\
произведите умножение kl и lk')
k = np.array([[5,8,-4],[6,9,-5],[4,7,-3]])
print(k)
l = np.array([[3,2,5],[4,-1,3],[9,6,5]])
print(l)

len_rows = len(k) # кол-во строк
len_cols = len(l[0]) # кол-во столбцов
output_matrix_kl = []
output_matrix_lk = []
for i in range(len_rows):
    row = []
    for j in range(len_cols):
        cur_cell = 0
        for t in range(len(k[0])):
            cur_cell += k[i][t]*l[t][j]
        row.append(cur_cell)
    output_matrix_kl.append(row)
print(f'k*l:\n{np.array(output_matrix_kl)}')
for i in range(len_rows):
    row = []
    for j in range(len_cols):
        cur_cell = 0
        for t in range(len(k[0])):
            cur_cell += l[i][t]*k[t][j]
        row.append(cur_cell)
    output_matrix_lk.append(row)
print(f'l*k:\n{np.array(output_matrix_lk)}')


