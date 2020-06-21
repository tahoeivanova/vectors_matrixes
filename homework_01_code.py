import numpy as np


# №1. Напишите функцию умножения трех матриц

def prod_matrix_3(matrix1, matrix2, matrix3):
    shape1 = matrix1.shape
    shape2 = matrix2.shape
    shape3 = matrix3.shape

    if ((shape1[1] != shape2[0]) or (shape2[1] != shape3[0])):
        return np.array([])

    # произведение первой и второй матрицы

    matrix1_2 = np.zeros([shape1[0], shape2[1]])

    for i in range(shape1[0]):
        for j in range(shape2[1]):
            cur_cell = 0
            for t in range(shape1[1]):
                cur_cell += matrix1[i][t] * matrix2[t][j]
                matrix1_2[i][j] = cur_cell

    # теперь умножить matrix1_2 на matrix3
    # matrix1_2 должна иметь один одщий шейп с matrix3

    shape1_2 = matrix1_2.shape

    out_matrix = np.zeros([shape1_2[0], shape3[1]])

    for i in range(shape1_2[0]):
        for j in range(shape3[1]):
            # cur_cell = 0
            for t in range(shape1_2[1]):
                cur_cell += matrix1_2[i][t] * matrix3[t][j]
                out_matrix[i][j] = cur_cell

    return out_matrix


# функция, которая выводит вектор без визуальных скобок
def print_vector(v):
    shape = v.shape

    # if (len(shape) == 0): # покажите пример, когда длина shape равна 0.
    # print(v)
    if (len(shape)) == 1:
        s = ''
        for i in v:
            s += str(i) + '  '
        print(s)
    if (len(shape) == 2):
        for i in range(shape[0]):
            s = ''
            for j in range(shape[1]):
                s += str(v[i][j]) + '  '
            print(s)
matrix1 = np.array([[0, 1, 2],[1, 2, 3],[2, 3, 4]])
matrix2 = np.array([[0, 1, 2, 3],[1, 2, 3, 4],[2, 3, 4, 5]])
matrix3 = np.array([[0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8]])

print("Первая матрица")
print_vector(matrix1)
print()
print("Вторая матрица")
print_vector(matrix2)
print()
print("Третья матрица")
print_vector(matrix3)
print()
print("Произведение трех матриц")
matrix_3 = prod_matrix_3(matrix1, matrix2, matrix3)
print_vector(matrix_3)


# №2. Напишите функцию, которая считает разницу между макимальным и минимальным элементами матрицы

def max_min_matrix(matrix):
    matrix_max = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] > matrix_max:
                matrix_max = matrix[i][j]
    print("Максимум матрицы: ", matrix_max)

    matrix_min = matrix_max
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] < matrix_min:
                matrix_min = matrix[i][j]
    print("Минимум матрицы: ", matrix_min)

    print("Разница между минимумом и максимумом матрицы равна: ", matrix_max - matrix_min)

print_vector(matrix1)
max_min_matrix(matrix1)
print()
print_vector(matrix2)
max_min_matrix(matrix2)
print()
print_vector(matrix3)
max_min_matrix(matrix3)


# №3. Напишите функцию, которая:
# умножает матрицу на саму себя, но транспонированную
#  функция, которая берет обратную матрицу от результата  - отдельно в последнем примере, выдает ошибку

def prod_transpose_matrix(matrix):
    shape = matrix.shape

    transpose_matrix = np.zeros((shape[1], shape[0]))
    for i in range(shape[0]):
        for j in range(shape[1]):
            transpose_matrix[j][i] = matrix[i][j]

    shape1 = matrix.shape
    shape2 = transpose_matrix.shape

    prod_matrix = np.zeros((shape1[0], shape2[1]))

    # проверку делать не надо, потому что матрица транспонированная

    for i in range(shape1[0]):
        for j in range(shape2[1]):
            cur_cell = 0
            for t in range(shape1[1]):
                # вопрос: как понять, от чего зависит - ставить i от t или t от i?
                cur_cell += matrix[i][t] * transpose_matrix[t][j]
                prod_matrix[i][j] = cur_cell

    return prod_matrix


# функция транспонирования матрицы
def transpose_matrix(matrix):
    shape = matrix.shape

    out_matrix = np.zeros((shape[1], shape[0]))

    for i in range(shape[0]):
        for j in range(shape[1]):
            out_matrix[j][i] = matrix[i][j]
    return out_matrix

print("Оригинальная матрица")
print_vector(matrix1)
print()
print("Транспонированная матрица")
matrix_trans = transpose_matrix(matrix1)
print_vector(matrix_trans)
print()
print("Матрица, умноженная на саму себя транспонированную")
matrix_trans_prod = prod_transpose_matrix(matrix1)
print_vector(matrix_trans_prod)
print()
print()
print("Оригинальная матрица")
print_vector(matrix3)
print()
print("Транспонированная матрица")
matrix_trans = transpose_matrix(matrix3)
print_vector(matrix_trans)
print()
print("Матрица, умноженная на саму себя транспонированную")
matrix_trans_prod = prod_transpose_matrix(matrix3)
print_vector(matrix_trans_prod)
print()


# Напишите функцию, которая:
# ( + ) умножает матрицу на саму себя, но транспонированную
#  ( - ) не работает: берет обратную матрицу от результата

def prod_transpose_matrix(matrix):
    shape = matrix.shape

    transpose_matrix = np.zeros((shape[1], shape[0]))
    for i in range(shape[0]):
        for j in range(shape[1]):
            transpose_matrix[j][i] = matrix[i][j]

    shape1 = matrix.shape
    shape2 = transpose_matrix.shape

    prod_matrix = np.zeros((shape1[0], shape2[1]))

    # проверку делать не надо, потому что матрица транспонированная

    for i in range(shape1[0]):
        for j in range(shape2[1]):
            cur_cell = 0
            for t in range(shape1[1]):
                cur_cell += matrix[i][t] * transpose_matrix[t][j]
                prod_matrix[i][j] = cur_cell

    inv_matrix = np.linalg.inv(prod_matrix)
    return inv_matrix

print("Оригинальная матрица")
print_vector(matrix2)
print()
print("Транспонированная матрица")
matrix_trans = transpose_matrix(matrix2)
print_vector(matrix_trans)
print()
print("Обратная матрице, умноженной на саму себя транспонированную")
matrix_trans_prod = prod_transpose_matrix(matrix2)
print_vector(matrix_trans_prod)
print()