import io
import sys

_INPUT = """\
2 3 4
"""
sys.stdin = io.StringIO(_INPUT)


# ---------------------------------------------------------------------------------------------------------

mod = 998244353

n, m, k = map(int, input().split())

dp = [[0] * (k + 1) for i in range(n + 1)]
print(dp)
dp[0][0] = 1

for i in range(n):
    for j in range(k):
        for k in range(1, m + 1):
            if k + j <= k:
                print(i, j)
                dp[i + 1][j + 1] += dp[i][j]

print(dp[n][k])
