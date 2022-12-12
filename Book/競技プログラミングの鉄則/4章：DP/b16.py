import io
import sys

_INPUT = """\
4
10 30 40 20
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

n = int(input())
h = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1] = 0
dp[2] = abs(h[1] - h[0])

for i in range(3, n + 1):
    dp[i] = min(
        dp[i - 1] + abs(h[i - 1] - h[i - 2]), dp[i - 2] + abs(h[i - 1] - h[i - 3])
    )
print(dp)
print(dp[-1])
