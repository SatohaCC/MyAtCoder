import io
import sys

_INPUT = """\
2
1 2 3
2 4 6
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 二次元配列を更新する動的計画法
# https://algo-method.com/tasks/41/editorial
# ---------------------------------------------------------------------------------------------------------
# 入力
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

c = len(A[0])
# 動的計画法の配列を用意する
dp = [[0] * c for _ in range(N)]

# 0 日目の情報をセットする
for i in range(c):
    dp[0][i] = A[0][i]

# 1, 2, ..., N-1 日目の報酬を求める
for i in range(1, N):
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + A[i][0]
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + A[i][1]
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + A[i][2]

# dp[N-1][0], dp[N-1][1], dp[N-1][2] の最大値を出力
print(max(dp[N - 1]))
