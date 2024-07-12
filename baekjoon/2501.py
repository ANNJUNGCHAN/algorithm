N, K = map(int, input().split(' '))

cnt = 0
for _ in range(1,N+1) :
    if N % _ == 0 :
        cnt += 1
        result = _
    else :
        pass
    if cnt == K :
        break
    
if cnt == K :
    print(result)
else :
    print(0)