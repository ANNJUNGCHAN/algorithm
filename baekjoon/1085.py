x,y,w,h = map(int, input().split())

# x가 w으로 가기
w_ = w-x
# y가 h으로 가기
h_ = h-y

all = [x, y, w_, h_]

print(min(all))