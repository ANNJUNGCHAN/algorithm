import sys

cnt = 0
for value in sys.stdin.readlines() :
    if cnt == 0 :
        moji = value
    else :
        num = int(value)
    cnt += 1
        
print(moji[num-1])