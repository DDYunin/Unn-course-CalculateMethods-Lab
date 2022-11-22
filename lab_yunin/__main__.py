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

# считает значение полинома (3*x^2+2*x+1) в точке
def polinom_func_1(x):
    return 3*(x**2)+2*x+1

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
def sympson_2(points):
    sum = 0
    print('Длина масиива points = {}'.format(len(points)))
    for index in range(0, len(points) - 2 , 2):
        sum += (points[index+2][0] - points[index][0])/6*(points[index][1] + 4*points[index+1][1] + points[index+2][1]) 
    return sum

    

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

def rule_3_of_8_2(points):
    sum = 0
    # у меня получается от нуля до n-1
    for index in range(0, len(points)-3, 3):
        sum += (points[index+3][0]-points[index][0])/8*(points[index][1]+3*points[index+1][1]+3*points[index+2][1]+points[index+3][1])
    return sum

def ThreeEighths(x, y):
    res = 0
    for i in range(0, x.size-3, 3):
        res+=(x[i+3]-x[i])/8*(y[i]+3*y[i+1]+3*y[i+2]+y[i+3])
    return res

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

def method_five_points_2(points):
    sum = 0
    for index in range(0, len(points)-4, 4):
        sum+=(points[index+4][0]-points[index][0])/90*(
            7*points[index][1]+32*points[index+1][1]+12*points[index+2][1]+32*points[index+3][1]+7*points[index+4][1]
            )
    return sum



def main():
    print('It is start')
    # sin_points = []
    # for index in range(30):
    #     sin_points.append([(math.pi / 29) * index, math.sin((math.pi / 29) * index)])
    # print(sin_points)
    # print('Ideal = 2')
    # print('The result with sympson = {0}'.format(sympson(sin_points)))
    # # print('The result with sympson_2 = {0}'.format(sympson_2(sin_points)))
    # print('The result with 3/8 rule = {0}'.format(rule_3_of_8(sin_points)))
    # print('The result with method five points = {0}'.format(method_five_points(sin_points)))
    #############################################
    polynom_points = []
    for index in range(30):
        polynom_points.append([index / 2,polinom_func_1(index / 2)])
    print(polynom_points)
    print('Ideal = 25259')
    print('The result with sympson = {0}'.format(sympson(polynom_points)))
    print('The result with 3/8 rule = {0}'.format(rule_3_of_8(polynom_points)))
    print('The result with method five points = {0}'.format(method_five_points(polynom_points)))
    # print(polinom_func_1(1))
    f = lambda x : 1 / math.sqrt(x) # 4
    Ans = 4
    x = np.linspace(1, 9, 25)
    y = np.vectorize(f)(x)
    print(x)
    print(y)
    points = []
    for i in range(0,25):
        points.append([1+1/3*i, f(1+1/3*i)])
    print(points)
    print('The result with sympson = {0}'.format(sympson(points)))
    print('The result with sympson_2 = {0}'.format(sympson_2(points)))
    print('The result with 3/8 rule = {0}'.format(rule_3_of_8(points)))
    print('The result with 3/8 rule_2 = {0}'.format(rule_3_of_8_2(points)))
    print('The result with method five points = {0}'.format(method_five_points(points)))
    print('The result with method five points_2 = {0}'.format(method_five_points_2(points)))

if __name__ == "__main__":
    main()