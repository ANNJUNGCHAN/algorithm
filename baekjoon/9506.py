while True :
    n = int(input())
    
    
    if n == -1 :
        break
    
    num = []
    
    for i in range(1,int(n/2) +1) :
        
        if n % i == 0 :
            num.append(i)
        
    if sum(num) == n :
        print(str(n) + " =", end = ' ')
        for idx in range(len(num)) :
            if idx < len(num) - 1 :
                print(str(num[idx]) + " + ", end= '')
            else :
                print(str(num[idx]))
                
    else :
        print(str(n) + " is NOT perfect.")
    
