import io
import sys

_INPUT = """\
4 7
3 13
3 17
5 29
1 10

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#  ナップザック問題 Knapsack
#
# ---------------------------------------------------------------------------------------------------------

# 入力
N, W = map(int, input().split())

w = [None] * (N + 1)
v = [None] * (N + 1)

for i in range(1, N + 1):
    w[i], v[i] = map(int, input().split())

# 動的計画法 マイナスで初期化しておく
dp = [[-(10**15)] * (W + 1) for i in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(0, W + 1):
        if j < w[i]:
            dp[i][j] = dp[i - 1][j]
        if j >= w[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])

# 出力
print(max(dp[N]))
