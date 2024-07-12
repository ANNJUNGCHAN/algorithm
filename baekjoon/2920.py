song = list(map(int,input().split(' ')))

rl = []

for idx, s in enumerate(song) :
    
    if idx == 0 :
        b = s
    
    else :
        r = b-s
        rl.append(r)
        b = s

rl = list(set(rl))

if len(rl) == 1 :
    if rl[0] == -1 :
        print('ascending')
    elif rl[0] == 1 :
        print('descending')

else :
    print('mixed')