# Дан двумерный массив точек (x,y) 
# получить, например, из известной функции
# Берётся интегрируемая по Риману функция
# То есть тем самым задана функция
# Нужно взять от неё интеграл 3 способами
# Формула Симпсона
# Формула 3/8
# Пятиточие
# Сравнить полученные результаты (погрешности)
# В качестве результата предъявить
# таблицы или графики
import math
import numpy as np


# Количество точек должно быть кратно 2
def sympson(points):
    h = (points[len(points) - 1][0] - points[0][0]) / len(points)
    sum = points[0][1] + points[len(points) - 1][1]
    for index in range(1, len(points)-1):
        if index % 2 == 1:
            sum += 4 * points[index][1]
        else:
            sum += 2 * points[index][1]
    sum *= h/3 
    return sum

# Количество точек должно быть кратно 2
# def sympson_2(points):
#     sum = 0
#     for index in range(0, len(points), 3):
#         sum += (points[index+2][0] - points[index][0])/6*(points[index][1] + 4*points[index][1] + points[index][1]) 
#     return sum

# количество точек должно быть кратно 3
def rule_3_of_8(points):
    h = (points[len(points) - 1][0] - points[0][0]) / len(points)
    sum = points[0][1] + points[len(points) - 1][1]
    for index in range(1, len(points) - 1):
        if index % 3 == 0:
            sum += 2 * points[index][1]
        else:
            sum += 3 * points[index][1]
    sum *= 3*h/8
    return sum

# def rule_3_of_8_2(points):
#     h = (points[len(points) - 1][0] - points[0][0]) / len(points)
#     sum = points[0][1] + points[len(points) - 1][1]
#     for index in range(1, len(points) - 1):
#         if index % 3 == 0:
#             sum += 2 * points[index][1]
#         else:
#             sum += 3 * points[index][1]
#     sum *= 3*h/8
#     return sum

# Количество точек должно быть кратно 4
def method_five_points(points):
    h = (points[len(points) - 1][0] - points[0][0]) / len(points)
    sum = 7*(points[0][1] + points[len(points) - 1][1])
    for index in range(1, len(points) - 1):
        if index % 4 == 2:
            sum += 12 * points[index][1]
        elif index % 4 == 0:
            sum += 14 * points[index][1]
        else:
            sum += 32 * points[index][1]
    sum *= 2*h/45
    return sum

# def method_five_points_2(points):
#     h = (points[len(points) - 1][0] - points[0][0]) / len(points)
#     sum = 7*(points[0][1] + points[len(points) - 1][1])
#     for index in range(1, len(points) - 1):
#         if index % 4 == 2:
#             sum += 12 * points[index][1]
#         elif index % 4 == 0:
#             sum += 14 * points[index][1]
#         else:
#             sum += 32 * points[index][1]
#     sum *= 2*h/45
#     return sum

def main():
    print('It is start')
    sin_points = []
    for index in range(30):
        sin_points.append([(math.pi / 29) * index, math.sin((math.pi / 29) * index)])
    print(sin_points)
    print('Ideal = 2')
    print('The result with sympson = {0}'.format(sympson(sin_points)))
    # print('The result with sympson_2 = {0}'.format(sympson_2(sin_points)))
    print('The result with 3/8 rule = {0}'.format(rule_3_of_8(sin_points)))
    print('The result with method five points = {0}'.format(method_five_points(sin_points)))


if __name__ == "__main__":
    main()