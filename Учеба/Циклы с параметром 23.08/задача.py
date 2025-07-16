


for N in range(100,1000):
    S = str(N)
    K1 = int(S[0]) + int(S[1])
    K2 = int(S[1]) + int(S[2])
    first = str(max(K1,K2))
    second = str(min(K1,K2))
    S1= first + second
    if S1 == '1412':
        print(N)
        break
    



