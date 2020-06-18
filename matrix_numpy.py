import numpy as np

'''
В библиотеке numpy есть поняте вектор.
Вектор представлен в виде numpy массива - np.array.
Чтобы создать вектор, нужно вызвать instance класса numpy, вызвать метод array
и передать на вход  в виде листа массив, который мы хотим создать.
'''

# создаем линейный вектор, состоящий из 4 координат
vector = np.array([1.3, 4.2, -2.2, 13.1])
# полученный вектор можем транспонировать
# reshape - изменение размера вектора
# сейчас размер: 1 строка6 4 элемента (1, 4)
# если мы хотим транспонировать, вызываем функцию reshape и указываем,
# что будет 4 строки, и в каждой по 1 элементу
vector_vertical = np.array([1.3, 4.2, -2.2, 13.1]).reshape((4,1))
print(f'Горизонтальный вектор: {vector}')
print(f'Вертикальный вектор:\n {vector_vertical}')

# shape - возвращает размер текущего вектора
print(vector.shape) # 4 элемента
print(vector_vertical.shape) # 4 строки по 1 элементу


# Скаляры
scalar1 = 1
scalar2 = 5
scalar3 = 17.345
scalar4 = -3.2476

print('Скаляры')
print(scalar1)
print(scalar2)
print(scalar3)
print(scalar4)

# функция для выведения векторов/матриц без скобок
def print_vector(v):
    shape = v.shape

    if (len(shape) == 0):
        print(v)

    if (len(shape) == 1):
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



# операции с векторами
# Добавление и вычитание скаляра
print(vector)
print(vector+1)
print(vector-1)

# Умножение на скаляр
print(vector*2)

# Деление на скаляр
print_vector(vector / 4)
# Возведение в степень
print_vector(vector ** 2)


# Сложение и вычитание векторов
vector1 = np.array([0,1,2,3])
vector2 = np.array([1,2,3,4])

print(vector1 + vector2)

# Умножение и деление векторов
print(vector1 * vector2)
print_vector(vector1 / vector2)
# Возведение в степень
print_vector(vector1 ** vector2)
# Пример матрицы
# Матрицы - это многомерный вектор

matrix = np.array([[1,2,3],
             [3,2,1],
             [0,0,1]
             ])
print(matrix)
print_vector(matrix)

# по матрице можно пробежаться в цикле

matrix2 = np.array([[145, 23, 191], [17, 252, 31], [99, 112, 39]])
print_vector(matrix2)
print(matrix2.shape)
# найдем максимум в матрице
matrix_max = 0

for i in range(matrix2.shape[0]): # количество строк
    for j in range(matrix2.shape[1]): # количество столбцов
        if matrix2[i, j] > matrix_max: # [i][j] - в numpy [i, j]
            matrix_max = matrix2[i, j]
print(matrix_max)


# Операции с матрицами
print('Операции с матрицами и скалярами')
print_vector(matrix)
print('Сложение')
print_vector(matrix+1)
print('Умножение')
print_vector(matrix*2)
print('Деление')
print_vector(matrix/4)
print('Возведение в степень')
print_vector(matrix**2)

print('Операции с двумя матрицами')
# 2 матрицы - это 2 numpy массива
print('Матрица 1')
print_vector(matrix)
print('Матрица 2')
print_vector(matrix2)
print()
print('Сложение')
print_vector(matrix + matrix2)

print()
print('Умножение')
print_vector(matrix * matrix2)

print()
print('Деление')
print_vector(matrix / matrix2)

print()
print('Возведение в степень')
print_vector(matrix2 ** matrix)





