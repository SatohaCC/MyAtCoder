import io
import sys

_INPUT = """\
2 1
90 80
70 60



"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------


r,c = map(int, input().split())
a=[]
for i in range(2):
    b= list(map(int, input().split()))
    a.append(b)

print(a[r-1][c-1])




