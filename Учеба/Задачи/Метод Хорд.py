         
print('Метод Хорд')

a = float(input('Введите левый конец промежутка изоляции: '))
b = float(input('Введите правый конец промежутка изоляции: '))
eps = float(input('Введите первое приблежение: '))
eps_1 = float(input('Введите второе приблежение: '))

def F(x):
    return x ** 2 + 3 * x - 4

def solve(a,b,eps,eps_1):
    x0 = a
    while 1:
        fa = F(a)
        fb = F(b)
        x = a - (b - a) * fa / (fb - fa)
        fx = F(x)
        if abs(fx) < eps_1:
            break
        if (fx * fa) < 0:
            b = x
        else:
            a = x
        if abs(x - x0) < eps:
            break
        x0 = x
    return x    
      
x = solve(a,b,eps,eps_1)       

print('Корень уравнения равен: {:.2f}'.format(x))