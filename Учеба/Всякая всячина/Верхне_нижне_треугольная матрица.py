from random import randint
N = 4
a = [[randint(1, 10) for j in range(N)] for i in range(N)]
for i in range (N): 
      for j in range ( len(a[i]) ):
          if i < j:
              a[i][j] = 0
          print ( "{:4d}".format(a[i][j]), end = "" ) 
      print ()
      
        