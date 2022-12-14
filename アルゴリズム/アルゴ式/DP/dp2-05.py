import io
import sys

_INPUT = """\
5
....#
...#.
..#..
.#...
#.... 
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

N = int(input())

G = [input() for _ in range(N)]


dp = [[0] * N for _ in range(N)]

# 初期値 (左上マスはすでに到達しているので 1 通り)
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        # 上から来る場合
        if i - 1 >= 0 and G[i - 1][j] != "#":
            dp[i][j] += dp[i - 1][j]
        # 左から来る場合
        if j - 1 >= 0 and G[i][j - 1] != "#":
            dp[i][j] += dp[i][j - 1]

print(dp[-1][-1])
