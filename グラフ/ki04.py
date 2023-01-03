import io
import sys

_INPUT = """\
4
1 2
2 3
3 4
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 葉の判定 (paizaランク C 相当)
# 「その頂点が葉である」→ 「その頂点に接続する辺が１本である」に言い換える
# ---------------------------------------------------------------------------------------------------------

N = int(input())
# N, X, Y = map(int, input().split())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]

G = [[0 for i in range(N)] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1][b - 1] = 1
    G[b - 1][a - 1] = 1


Ans = [0 for i in range(N)]

for i in range(N):
    c = 0
    for j in range(N):
        if G[i][j]:
            c += 1
    Ans[i] = c

for i in range(N):
    if Ans[i] == 1:
        print(i + 1)
