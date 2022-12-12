# 最短何分かかるか

import io
import sys

_INPUT = """\
10
1 19 75 37 17 16 33 18 22
41 28 89 74 98 43 42 31
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0 for i in range(n + 1)]

dp[2] = a[0]
for i in range(3, n + 1):
    dp[i] = min(dp[i - 1] + a[i - 2], dp[i - 2] + b[i - 3])


print(dp[-1])
