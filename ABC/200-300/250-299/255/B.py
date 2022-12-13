import io
import sys

_INPUT = """\
8 3
2 6 8
-17683 17993
93038 47074
58079 -57520
-41515 -89802
-72739 68805
24324 -73073
71049 72103
47863 19268


"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------
import math
n,k = map(int, input().split())

a = list(map(int, input().split()))

x=[]
for i in range(n):
    b = list(map(int, input().split()))
    x.append(b)

targets = []
for i in a:
    targets.append(x[i-1])

q=[]

for c in x:
    tmp = 100000000000000000000000000000000000
    for target in targets:
        bright = math.sqrt((target[0]-c[0])*(target[0]-c[0]) + (target[1]-c[1])*(target[1]-c[1]))
        if bright!=0:
            tmp = min(bright,tmp)
    q.append(tmp)
    print(q)

print(max(q))