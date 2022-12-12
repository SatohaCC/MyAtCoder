# ２次元の累積和
# 累積和で求めることですぐに最大が求められる


import io
import sys


_INPUT = """\
7
1 2 5 5 2 3 1
2
1 7
4 6
"""
sys.stdin = io.StringIO(_INPUT)

# 入力
N = int(input())
A = list(map(int, input().split()))
D = int(input())


# 左からの最大値
P = [0] * (N + 2)
for i in range(N):
    P[i + 1] = max(P[i], A[i])


# 右からの最大値
Q = [0] * (N + 2)
for i in range(-1, -N - 1, -1):
    Q[i - 1] = max(Q[i], A[i])

# 出力
for i in range(D):
    L, R = list(map(int, input().split()))
    print(max(P[L - 1], Q[R + 1]))
