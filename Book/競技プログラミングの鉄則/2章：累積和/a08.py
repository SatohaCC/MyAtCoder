# ２次元の累積和
# pythonで[[]] * 11のように積で配列を多数生成しようとすると、
# 同じIDのものが複製されるため、どれかを変更すると全て同じように変更されてしまいます。
#


import io
import sys


_INPUT = """\
5 5
2 0 0 5 1
1 0 3 0 0
0 8 5 0 2
4 1 0 0 6
0 9 2 7 0
2
2 2 4 5
1 1 5 5
"""
sys.stdin = io.StringIO(_INPUT)

h, w = map(int, input().split())
# a = list(map(int, input().split()))

# 配列初期化
cumulative = [[0 for i in range(w + 1)] for j in range(h + 1)]

# 入力・横の累積和
for i in range(1, h + 1):
    tmp_row = list(map(int, input().split()))
    for j in range(1, w + 1):
        cumulative[i][j] = cumulative[i][j - 1] + tmp_row[j - 1]

# 縦の累積和
for i in range(1, h + 1):
    for j in range(1, w + 1):
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
