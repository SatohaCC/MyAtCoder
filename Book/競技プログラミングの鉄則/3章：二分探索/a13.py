# A13 - Close Pairs
# しゃくとり法

import io
import sys

_INPUT = """\
7 10
1 12 16 22 27 28 31


"""
sys.stdin = io.StringIO(_INPUT)

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

# 配列の準備（R は 0 番目から始まることに注意）
R = [None] * N

# しゃくとり法
for i in range(0, N - 1):
    print("i:", i, "        R[i-1]:", R[i - 1])
    # print(i, R)
    # スタート地点を決める
    if i == 0:
        R[i] = 0
    else:
        R[i] = R[i - 1]

    # ギリギリまで増やしていく
    while (R[i] < N - 1) and (A[R[i] + 1] - A[i] <= K):
        R[i] += 1
        print("i:", i, "        R[i]:", R[i])

    print()
# 出力
Answer = 0
for i in range(0, N - 1):
    Answer += R[i] - i
print(Answer)
