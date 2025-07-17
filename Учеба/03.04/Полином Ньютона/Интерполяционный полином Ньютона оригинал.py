print('Интерполяционный полином Ньютона оригинал')


def newton_interpolation(x_values, y_values, x):
    """
    :param x_values: список значений x
    :param y_values: список значений y
    :param x: значение, для которого нужно найти приближенное значение y
    :return: приближенное значение y, рассчитанное с помощью интерполяционного полинома Ньютона
    """
    n = len(x_values)
    # Инициализация разделенных разностей
    f = [[None] * n for _ in range(n)]
    for i in range(n):
        f[i][0] = y_values[i]
    # Вычисление разделенных разностей
    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i+1][j-1] - f[i][j-1]) / (x_values[i+j] - x_values[i])
    # Вывод таблицы конечных разностей
    print("Таблица конечных разностей:")
    for row in f:
        for elem in row:
            if elem is not None:
                print("{:.4f}".format(elem), end="\t")
            else:
                print("\t", end="")
        print()
    # Вычисление значения интерполяционного полинома
    y = 0
    for i in range(n):
        prod = f[0][i]
        for j in range(i):
            prod *= (x - x_values[j])
        y += prod
    return y

x_values = [0,1,2,3,4]
y_values = [1,4,15,40,85]
x = 1.5
y = newton_interpolation(x_values, y_values, x)
print("Значение интерполяционного полинома в точке x = {:.2f}: {:.4f}".format(x, y))