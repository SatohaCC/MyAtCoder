# B13 - Supermarket 2
# しゃくとり法 ・累積和

import io
import sys

_INPUT = """\
7 6
4
3
1
1
2
10
2
"""

sys.stdin = io.StringIO(_INPUT)


N, K = list(map(int, input().split()))
A = []

for i in range(N):
    A.append(int(input()))


# 配列の準備（R は 0 番目から始まることに注意）
R = [0] * N

# しゃくとり法
for i in range(0, N):
    # print(i, R)
    # スタート地点を決める

    # ギリギリまで増やしていく
    print(i, " : ", R[i], N, "    ", A[i], A[R[i] + 1])
    while (R[i] < N) and (A[i] * A[R[i] + 1] <= K):
        print(R[i], N, "    ", A[i], A[R[i] + 1])
        R[i] += 1
    print()

# 出力
Answer = 0
for i in range(0, N - 1):
    Answer += R[i] - i
print(Answer)
