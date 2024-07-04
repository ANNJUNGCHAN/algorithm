import sys

cnt = 0
rec = 0
for value in sys.stdin.readlines() :
    ### 전체 금액
    if cnt == 0 :
        total_money = int(value)
    
    ### 전체 품목
    elif cnt == 1 :
        total_count = int(value)
        
    ### 각각의 금액
    else :
        money, count = value.split(' ')
        rec += int(money) * int(count)
        
    cnt += 1
    
if total_money == rec :
    print("Yes")
    
else :
    print("No")