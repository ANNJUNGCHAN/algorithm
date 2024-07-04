import sys

cnt = 0
row = 0

for value in sys.stdin.readlines() :
    line = list(map(int,value.split(' ')))
    
    if cnt == 0 :
        max_value = max(line)
        index = line.index(max_value)
    
    else :
        next_max_value = max(line)
        next_index = line.index(next_max_value)
        
        if max_value < next_max_value :
            max_value = next_max_value
            index = next_index
            row = cnt
        
    cnt += 1

print(max_value)
print(row + 1, index + 1)