N, B = map(int, input().split(' '))

k = 0
while True :
    if N < B ** k :
        break
    else :
        k += 1
        
k_list = [_ for _ in range(k)]
k_list.reverse()

result = ""
for k_temp in k_list :
    res = N // (B ** k_temp)
    N -= res * (B ** k_temp)
    if res < 10 :
        result += str(res)
    else :
        result += chr(res - 10 + ord('A'))
        
print(result)