import io
import sys

_INPUT = """\
8
3 1 4 1 5 9 2 6
"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------


n = int(input())

a = list(map(int, input().split()))

dp =[0]*n
dp[0] = 0
dp[1] = a[1]
for i in range(2,n):
    dp[i] = min(dp[i-1]+a[i],dp[i-2]+a[i]*2)

print(dp[-1])