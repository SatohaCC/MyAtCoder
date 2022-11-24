import io
import sys

_INPUT = """\
1000000000 314 159
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------



n,a,b = map(int, input().split())
ans=0
c = a*b
for i in range(1,n+1):
    if i%a !=0 :
        if i%b !=0:
            ans +=i

print(ans)