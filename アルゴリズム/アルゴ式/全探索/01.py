import io
import sys

_INPUT = """\
10
1 5 2 9 6 4 9 3 4 9
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

N = int(input())

A = list(map(int, input().split()))

c = [0] * 9
for i in range(N):
    c[A[i] - 1] += 1

ans = 0
for i in range(9):
    if c[ans] < c[i]:
        ans = i

print(ans + 1)
