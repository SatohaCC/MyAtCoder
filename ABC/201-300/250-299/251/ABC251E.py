import io
import sys

_INPUT = """\
20
2 5 3 2 5
"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------



n = int(input())

a = list(map(int, input().split()))


dp=[0 for _ in range(n)]
print(dp)
tmp=0
c=0
for i in range(0,n):
    c+=1
    print(c,i)
    if c in [1,2,4]:
        print(" ",i)
    if c==5:
        c=0