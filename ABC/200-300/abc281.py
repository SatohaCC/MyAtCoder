import io
import sys

_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 累積和、二分探索
#
# ---------------------------------------------------------------------------------------------------------

from bisect import bisect

N, T = map(int, input().split())
a = list(map(int, input().split()))

b = [0 for _ in range(N + 1)]
b[1] = a[0]
for i in range(1, N + 1):
    b[i] = b[i - 1] + a[i - 1]


if T > b[-1]:
    T = T % b[-1]

tmp = bisect(b, T)
print(tmp, T - b[tmp - 1])
