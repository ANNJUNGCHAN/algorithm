import sys

cnt = 0
for value in sys.stdin.readlines() :
    
    if cnt == 0 :
        N, M = map(int, value.split(' '))
        box = [_ for _ in range(1, N+1)]
        
    else :
        i, j = map(int, value.split(' '))
        i_value = box[i-1]
        j_value = box[j-1]
        box[j-1] = i_value
        box[i-1] = j_value
    cnt += 1

for _ in box :
    print(_, end = ' ')