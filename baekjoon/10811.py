import sys

cnt = 0
for value in sys.stdin.readlines() :
    
    if cnt == 0 :
        N, M = map(int, value.split(' '))
        box = [_ for _ in range(1,N+1)]
        
    else :
        i, j = map(int, value.split(' '))
        cbox = box[i-1:j]
        cbox.reverse()
        box[i-1:j] = cbox

        
    cnt += 1
    
for _ in box :
    print(_, end = ' ')