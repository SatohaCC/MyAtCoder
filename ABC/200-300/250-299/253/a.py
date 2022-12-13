import io
import sys

_INPUT = """\
5 5
3 5 5 9 5
"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------

n,v = map(int, input().split())

a = list(map(int, input().split()))

index =-1

for i in range(n):
    if v == a[i]:
        index = i

print(index)