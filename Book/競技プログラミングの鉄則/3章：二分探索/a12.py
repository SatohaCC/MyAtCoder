# A12 - Printer
# 答えに二分探索するパターン
# 自分でACできずに答え見た

import io
import sys


_INPUT = """\
10 10
1 1 1 1 1 1 1 1 1 1
"""
sys.stdin = io.StringIO(_INPUT)


def check(x, N, K, A):
    sum = 0
    for i in range(N):
        sum += x // A[i]

    if sum >= K:
        return True
    return False


# 入力
N, K = map(int, input().split())
A = list(map(int, input().split()))


Left = 1
Right = 10**9

while Left < Right:
    Mid = (Left + Right) // 2
    Answer = check(Mid, N, K, A)

    if Answer:
        Right = Mid
    else:
        Left = Mid + 1

print(Left)
