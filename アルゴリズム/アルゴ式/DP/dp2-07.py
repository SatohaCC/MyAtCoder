import io
import sys

_INPUT = """\
5
10 1 1 1 1
10 10 1 1 1
1 10 10 1 1
1 1 10 10 1
1 1 1 10 10
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 右上から左下は入力で反転してあげると簡単になる
#
# ---------------------------------------------------------------------------------------------------------
# 入力
N = int(input())
field = []
for i in range(N):
    a = list(map(int, input().split()))
    a.reverse()
    field.append(a)


# DP 配列の定義 (配列全体を 0 で初期化)
dp = [[99999999999] * N for _ in range(N)]

# 初期値 (左上のマスの値をセット)
dp[0][0] = field[0][0]

# マスを順に埋めていく
for i in range(N):
    for j in range(N):
        # 上から来る場合
        if i - 1 >= 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + field[i][j])

        # 左から来る場合
        if j - 1 >= 0:
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + field[i][j])

# 出力
print(dp[N - 1][N - 1])
