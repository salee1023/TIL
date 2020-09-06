import math

ball = [
    [100, 100], # ball 1
    [0, 200] # ball 2
]
x = ball[1][0] - ball[0][0]
y = ball[1][1] - ball[0][1]
# x = 1
# y = -1
d = math.degrees(math.atan2(y, x))
print(d)
if x < 0 and y > 0:
    ans = 90-d+360
else:
    ans = 90-d

print(ans)


# 각도구하기
'''
import math
rad = math.atan(y,x) # y/x
rad = math.tan(y.x)
gakdo = math.degrees(rad)
distance = math.sqrt(x**2 + y**2)
'''