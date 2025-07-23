print('Таблича первых 127 занчений ASCII')

for i in range(0,128):
    print((i,chr(i)), end='')
    if i % 3 == 0:
        print()
     
print()