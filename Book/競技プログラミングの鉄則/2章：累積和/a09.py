# ２次元の累積和
# +2でから配列作成


import io
import sys


_INPUT = """\
5 5 2
1 1 4 4
1 1 5 5

"""
sys.stdin = io.StringIO(_INPUT)

# 入力
H, W, N = map(int, input().split())
A = [None] * N
B = [None] * N
C = [None] * N
D = [None] * N


for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())


# 配列初期化
tmp = [[0 for i in range(W + 2)] for j in range(H + 2)]
ans = [[0 for i in range(W + 2)] for j in range(H + 2)]


for i in range(N):
    tmp[A[i]][B[i]] += 1
    tmp[C[i] + 1][D[i] + 1] += 1
    tmp[A[i]][D[i] + 1] -= 1
    tmp[C[i] + 1][B[i]] -= 1


# 横の累積和
for i in range(1, H + 2):
    for j in range(1, W + 2):
        ans[i][j] = ans[i][j - 1] + tmp[i][j]

# 縦の累積和
for i in range(1, H + 2):
    for j in range(1, W + 2):
        ans[i][j] = ans[i - 1][j] + ans[i][j]

# 出力：0列目を出力しないようにスライス
for i in range(1, H + 1):
    print(*ans[i][1 : W + 1])
