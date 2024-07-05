N, B = map(str, input().split(' '))

result = 0
num_list = [str(_) for _ in range(0,10)]
### 문자열 뒤집는 방법을 알고가자!
N = ''.join(reversed(N))

for idx, digit in enumerate(N) :
    if digit in num_list :
        result += ((int(digit)) * (int(B) ** (idx)))
    else :
        result += ((ord(digit) - ord('A')) + 10) * (int(B) ** (idx))
        
print(result)