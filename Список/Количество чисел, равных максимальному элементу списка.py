print('Количество чисел, равных максимальному элементу списка')

N = int(input('Введите количество элементов списка: '))
A = [int(input('Введите значение: ')) for i in range(N)]
print(A)

count = 0
Max = A[0]       
for i in A: 
    if i > Max:
        Max = i
for x in A:
    if x == Max:
        count += 1
print('Максимальное значение списка А, равно',Max) 
print(count,'Раза встречается число',Max,'в списке') 