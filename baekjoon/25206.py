import sys

cnt = 0
total = 0
table = {'A' : 4, 'B' : 3, 'C' : 2, 'D' : 1, 'F' : 0}
for value in sys.stdin.readlines() :
    _, count, grade = map(str, value.split(' '))
    
    if grade[0] != 'P':
        
        base = table[grade[0]]
        
        if len(grade) >1:
            if grade[1] == '+' :
                base += 0.5
            
        total += base * int(float(count))
        cnt += int(float(count))

print(round(float(total/cnt),6))