N, K = map(int, input().split(' '))

rl = []
for i in range(1,int(N ** (1/2)) + 1) :
    if N % i == 0 :
        rl.append(i)
        if i < N//i :
            rl.append(N // i) 
rl.sort()
try :
    print(rl[K-1])
except :
    print(0)