import sys

str_list = []
str_len_list = []
for value in sys.stdin.readlines() :
    value = value.replace('\n','')
    str_list.append(value)
    str_len_list.append(len(value))
    
max_len = max(str_len_list)

reverse = ["" for _ in range(max_len)]

for s in str_list :
    for _ in range(max_len) :
        try :
            reverse[_] += s[_]
        except :
            reverse[_] += " "
        
result = ""

for x in reverse :
    result += x

result = result.replace(" ","")
print(result)