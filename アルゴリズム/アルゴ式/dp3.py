import io
import sys

_INPUT = """\
10
"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------


n = int(input())

dp = [0]*(n+1)

dp[0] = 1
dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp)
print(dp[-1])