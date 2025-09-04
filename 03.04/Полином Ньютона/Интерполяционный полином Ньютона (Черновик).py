print('Интерполяционный полином Ньютона (Черновик)')

x = [0,1,2,3,4]
y = [1,4,15,40,85]



n = len(x) 
Y = [ ]
Y.append(y[0])
def delta_y(y):
    y_d = [ ]
    for i in range(len(y)-1):
        yd = y[i+1] - y[i]
        y_d.append(yd)
    return y_d
while len(y) != 1:
    y = delta_y(y)
    Y.append(y[0])  
    
print(Y)    
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact 
for i in range(n-1):
    print(i)
    print(Y[i])
    print(factorial(i+1))
    sigm = Y[i] / factorial(i+1) * (x[i + 1] - x[i]) ** i
    print('разности - ',sigm)
  