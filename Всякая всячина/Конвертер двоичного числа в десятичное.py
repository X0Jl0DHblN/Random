print('Конвертер двоичного числа в десятичное')

n = input('Введите двоичное число и нажмите Enter: ')
int_n = 0
N = n[::-1]
L = len(n)
print(L)

for i in (N):
    #print(i, end = '')
    L = L-1
    print(L)
    int_1 = int(i) * 2**L
    #print(int_1)
    int_n = int(int_n) + int(int_1)
    #int_n = int_n + i*
print(int_n)    