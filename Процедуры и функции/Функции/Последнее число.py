print('Последнее число')

N = int(input('Введите число: ')) 

def last_digit(n):
    x = n % 10
    return x

Num = last_digit(N)
print(Num)