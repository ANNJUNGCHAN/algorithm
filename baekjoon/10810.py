import sys

cnt = 0

for value in sys.stdin.readlines() :
    
    if cnt == 0 :
        N, M = map(int,value.split(' '))
        basket = [0 for _ in range(N)]
    
    else:
        i, j ,k = map(int,value.split(' '))
        for basket_num in range(i-1,j) :
            basket[basket_num] = k
    cnt += 1

### 여기 부분!! ###
for i in range(len(basket)) :
    print(basket[i], end = ' ')

### print문에서 end조건을 걸면, 해당 문자가 끝날때마다 어떤 것으로 끝날 지 확인가능!!"
        