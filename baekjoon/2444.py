value = 2 * int(input()) - 1

for n in range(1,value+1) :
    
    if n <= int(value/2) + 1 :
        star = 2 * (n -1) + 1
        blank = int((value - star) / 2)
        print(blank * ' ' + star * '*')
        
    else :
        star = (value - n) * 2 + 1
        blank = int((value - star) / 2)
        print(blank * ' ' + star * '*')