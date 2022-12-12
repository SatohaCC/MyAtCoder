import io
import sys

_INPUT = """\
3 100
55 2
75 3
40 2


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# ナップザック問題 Knapsack
# 重さの総和の最小値
# ---------------------------------------------------------------------------------------------------------

# 入力
N, W = map(int, input().split())
w = [None] * (N + 1)
v = [None] * (N + 1)

for i in range(1, N + 1):
    w[i], v[i] = map(int, input().split())

MAX = 100 * 1000 + 1

# 動的計画法
dp = [[10**15] * MAX for i in range(N + 1)]


dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(MAX):
        if j < v[i]:
            dp[i][j] = dp[i - 1][j]
        if j >= v[i]:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - v[i]] + w[i])

# 出力
Answer = 0
for j in range(MAX):
    if dp[N][j] <= W:
        Answer = j
        print(dp[N][j])

print(Answer)
