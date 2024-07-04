value = input()
reverse = []
for v in value :
    reverse.append(v)

reverse.reverse()

reverse_value  = ""
for r in reverse :
    reverse_value += r

if value == reverse_value :
    print(1)

else :
    print(0)