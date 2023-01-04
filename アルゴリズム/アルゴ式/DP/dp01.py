import io
import sys

_INPUT = """\
8
3 1 4 1 5 9 2 6
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

N = int(input())
# N, X, Y = map(int, input().split())
# A, B = map(int, input().split())
A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]


dp = [0] * (N)
dp[1] = A[1]

for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + A[i] * 2)

# print(dp)
print(dp[N - 1])
