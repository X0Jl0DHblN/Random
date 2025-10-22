
N = int(input('Введите количество элементов в очереди: '))

A = [ ]
for x in range(N):
    x = int(input('Введите значение: '))
    A.append(x)
A.reverse()
print(A) 
print()
print('Первый элемент очереди {}'.format(A[-1]))
print()
print('Требуется ли удалить элемент из очереди?')
print('Y - удалить, N - не удалять')
ch = input()
if ch == 'Y':
    n = int(input('Введите количество элементов очереди для удаления: '))
    for i in range(n):
        print('Элемент {} удален из очереди'.format(A.pop(-1)))
if 0 < len(A) != 1:
    print('Первый и последний элемент очереди {} и {}'.format(A[-1], A[0]))
elif len(A) == 1:
    print('В очереди один элемент ->', A[0])
else:
    print('Очередь пуста')
                