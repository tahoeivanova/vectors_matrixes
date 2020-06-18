import numpy as np
from copy import deepcopy

class Matrix:
    # принимает на вход матрицу в виде np листа
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix) # количество строк
        self.m = len(matrix[0]) # количество столбцов

    #  умножение матрицы на скаляр
    # умножаем каждое значение матрицы на скаляр
    def scalar_multiplier(self, scalar):
        # в цикле проходим по всей матрице
        for i in range(self.n): # итерируемся по строкам матрицы
            row = []
            # для каждой строки будем выполнять умножение каждого
            # элемента этой строки
            for j in range(self.m):
                # когда проходим по каждому столбцу,
                # выполняем умножение на скаляр и добавляем этот элемент в новую строчку
                row.append(self.matrix[i][j] * scalar)
            # берем каждую строчку матрицы и ее перезаписываем поэлементно
            # и меняем значение строки исходной матрицы на новую
            self.matrix[i] = row

    def T(self):
        # скопируем с помощью deepcopy матрицу в переменную transpose
        transpose = deepcopy(self.matrix)
        # пройдемся по каждой строчке
        for i in range(self.n):
            # пройдемся по каждому столбцу
            for j in range(self.m):
                # внесем в новую матрицу transpose:
                # повернем наши строчки по часовой стрелке
                transpose[i][j] = self.matrix[j][i]
        return transpose

m1 = Matrix([[1,2,3],
             [3,2,1],
             [0,0,1]
             ])

print(m1.matrix)
print(m1.T()) # столбец [1, 3, 0] стал строкой

m1.scalar_multiplier(-1)
print(m1.matrix)
m1.scalar_multiplier(-1)
print(m1.matrix)



# сложение двух матриц
def matrix_add(m1, m2):
    # копируем исходную матрицу №1
    new_m = deepcopy(m1.matrix)
    # пройдемся по каждой строке и по каждому столбцу матриц
    # и внесем в новую матрицу сумму элементов двух матриц
    for i in range(m1.n):
        for j in range(m1.m):
            new_m[i][j] = m1.matrix[i][j]+m2.matrix[i][j]
    return new_m


print(matrix_add(m1,m1))



def prod_matrix(m1,m2):
    # кол-во строк m1 при произведении
    # соответсвует количеству столбцов m2
    n = m1.n # количество строк матрицы 1
    m = m2.m # количество столбцов матрицы 2

    out_matrix = [] # выходной массив

    for i in range(n): # проходим по каждой строчке результирующей матрицы
        # на каждом проходе инициализируем пустую переменную row,
        # в которую будем записывать все элементы конкретной строки
        row = []
        # для каждого столбца, который будет в новой матрице
        for j in range(m):
            cur_cell = 0
            # пробегаемся по всем столбцам матрицы 1
            for t in range(m1.m):
                # получаем их координаты
                # и добавляем в переменную cur_cell произведение элемента матрицы 1 из строки m и столбца t
                # и элемента матрицы 2 из строки t и столбца j
                cur_cell += m1.matrix[i][t] * m2.matrix[t][j]
            row.append(cur_cell)
        out_matrix.append(row)
    return out_matrix

print(prod_matrix(m1,m1))


# Найти произведение матрицы k = [[2,-3],[4,-6]] и l = [[9,-6],[6,-4]]

k = Matrix([[2,-3],
            [4,-6]
            ])
l = Matrix([[9,-6],
            [6,-4]
            ])

print(prod_matrix(k,l))

# перестановка матриц в произведении дает другой результат
print(prod_matrix(l, k))

# Обратная матрица

inverted_matrix = Matrix(np.linalg.inv(m1.matrix).tolist())
print(inverted_matrix.matrix)
e0= prod_matrix(inverted_matrix,m1)
print(e0)
E = np.array(prod_matrix(inverted_matrix,m1), dtype='float16')
print(E)


