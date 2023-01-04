import io
import sys

_INPUT = """\
9 9 9 9  

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 二次元配列を更新する動的計画法
#
# ---------------------------------------------------------------------------------------------------------

A = list(map(int, input().split()))
N = len(A)

dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[0][i] = A[i]

for i in range(1, N):
    for j in range(N):
        # 真上を足す
        dp[i][j] += +dp[i - 1][j]
        # 左上を足す
        if j - 1 >= 0:
            dp[i][j] += dp[i - 1][j - 1]
        # 右上を足す
        if j + 1 < N:
            dp[i][j] += dp[i - 1][j + 1]
print(dp[-1][-1])
