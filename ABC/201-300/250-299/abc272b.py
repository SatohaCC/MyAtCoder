import io
import sys

_INPUT = """\
4 2
3 1 2 4
3 2 3 4


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 二次元配列 ３重ループ
# ２人の組み合わせ
# ---------------------------------------------------------------------------------------------------------

N, M = map(int, input().split())

tmp = [[0 for i in range(N + 1)] for i in range(N + 1)]

for i in range(M):
    a, *b = list(map(int, input().split()))
    for i in range(a):
        for j in range(i + 1, a):
            tmp[b[i]][b[j]] = 1
            tmp[b[j]][b[i]] = 1

for i in range(1, N):
    if tmp[i].count(1) != N - 1:
        print("No")
        exit()

print("Yes")
