print('Количество цифр в введенном числе')

N = int(input("Введите число: "))

def numberOfDigits(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    return count

print("Количество цифр равно: ", numberOfDigits(N))