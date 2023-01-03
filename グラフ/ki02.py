import io
import sys

_INPUT = """\
10
1 2
2 3
3 4
4 5
6 5
7 6
8 7
9 8
10 9
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 木の入力の受け取り（隣接リスト）
# グラフ (N 頂点) の隣接リストとは、
# N 本の連結リスト g_1, ... g_n であって、
# 各頂点 i について g_i が 「頂点 i と直接辺で繋がれている頂点のリスト」になっているようなものを指します。
# ---------------------------------------------------------------------------------------------------------

N = int(input())

G = [[0 for i in range(N)] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1][b - 1] = 1
    G[b - 1][a - 1] = 1

Ans = [list() for i in range(N)]

for i in range(N):
    for j in range(N):
        if G[i][j]:
            Ans[i].append(j + 1)

for i in range(N):
    print(*Ans[i])
