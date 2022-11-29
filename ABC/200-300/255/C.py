import io
import sys

_INPUT = """\
-555555555555555555 -1000000000000000000 1000000 1000000000000


"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------


from bisect import bisect_left, bisect_right
x,a,d,n= map(int, input().split())

print
A = []
A.append(a)
A.append(a+d*n)

A = sorted(A)
print(A)
ans = 0
if A[0] > x:
    ans = A[0] - x
elif x > A[-1]:
    ans = x - A[-1]
elif A[0] < x < A[-1]:
    c = x//d
    print(c)


print(ans)