# ２次元の累積和
# pythonで[[]] * 11のように積で配列を多数生成しようとすると、
# 同じIDのものが複製されるため、どれかを変更すると全て同じように変更されてしまいます。


import io
import sys

_INPUT = """\
5
1 3
2 5
3 4
2 6
3 3
3
1 3 3 6
1 5 2 6
1 3 3 5
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())


# 配列初期化
cumulative = [[0 for i in range(1500 + 1)] for j in range(1500 + 1)]


# 入力
for i in range(N):
    X, Y = map(int, input().split())
    cumulative[X][Y] += 1


# 横累積和
for i in range(1500 + 1):
    for j in range(1500 + 1):
        cumulative[i][j] = cumulative[i][j - 1] + cumulative[i][j]

# 横累積和
for i in range(1500 + 1):
    for j in range(1500 + 1):
        cumulative[i][j] = cumulative[i - 1][j] + cumulative[i][j]


# クエリ
Q = int(input())

for i in range(Q):
    a, b, c, d = map(int, input().split())
    ans = (
        cumulative[c][d]
        + cumulative[a - 1][b - 1]
        - cumulative[a - 1][d]
        - cumulative[c][b - 1]
    )
    print(ans)
