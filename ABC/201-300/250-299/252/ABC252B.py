import io
import sys

_INPUT = """\
5 2
100 100 100 1 1
5 4

"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------


n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_max = max(a)

ans = True
for i in b:
    if a[i-1] == a_max:
        ans = True
        break
    else:
        ans = False

if ans:
    print("Yes")
else:
    print('No')