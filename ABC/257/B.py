import io
import sys

_INPUT = """\
5 3 5
1 3 4
3 3 1 1 2

"""
sys.stdin = io.StringIO(_INPUT)
import io
_INPUT = """\ 
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------------------------------------------------------------------------------
n = int(input())
n,x, a,y, b = map(int, input().split())
a = list(map(int, input().split()))


# ---------------------------------------------------------------------------------------------------------

n,k,q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

m = [0]*(n+1)

for i in range(k):
    m[a[i]] = i+1

for j in range(q):
    for i in range(n):
        if m[i] == l[j] and m[i+1] == 0:
            m[i],m[i+1] =0, m[i]
            break
for i in range(1,n+1):
    if m[i] !=0:
        print(i,end=' ')