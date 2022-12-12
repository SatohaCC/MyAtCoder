# ２次元の累積和
# 最小と最大に気をつける


import io
import sys


_INPUT = """\
2
0 0 5 5
2 2 4 4
"""
sys.stdin = io.StringIO(_INPUT)

# 入力
N = int(input())
A = [None] * (N + 1)
B = [None] * (N + 1)
C = [None] * (N + 1)
D = [None] * (N + 1)

for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())


MAX = 1501
# 配列初期化
tmp = [[0] * MAX for j in range(MAX)]
cumulative = [[0 for i in range(MAX)] for j in range(MAX)]


for i in range(N):
    tmp[A[i]][B[i]] += 1
    tmp[C[i]][D[i]] += 1
    tmp[A[i]][D[i]] -= 1
    tmp[C[i]][B[i]] -= 1


# 横の累積和
for i in range(0, MAX):
    for j in range(1, MAX):
        tmp[i][j] = tmp[i][j - 1] + tmp[i][j]


# 縦の累積和
for i in range(1, MAX):
    for j in range(0, MAX):
        tmp[i][j] = tmp[i - 1][j] + tmp[i][j]


# 出力
ans = 0
for i in range(0, MAX):
    for j in range(0, MAX):
        if tmp[i][j] >= 1:
            ans += 1
print(ans)
