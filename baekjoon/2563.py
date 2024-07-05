import sys

cnt = 0

black_box = []
for value in sys.stdin.readlines() :
    
    if cnt == 0 :
        N = int(value)

    else :
        w_start, h_start = map(int,value.split(' '))
        
        for w_element in range(w_start+1, w_start + 10 + 1) :
            for h_element in range(h_start+1, h_start +10 +1) :
                if [w_element, h_element] not in black_box :
                    black_box.append([w_element, h_element])
                    
    cnt += 1
    
print(len(black_box))