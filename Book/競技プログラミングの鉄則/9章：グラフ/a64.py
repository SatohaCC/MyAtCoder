import io
import sys

_INPUT = """\
15 30
10 11 23
11 13 24
5 8 22
10 15 18
12 14 15
2 10 11
4 7 15
5 7 15
7 9 8
8 12 1
5 14 1
10 14 17
10 12 11
8 10 6
7 14 28
6 9 1
1 10 19
4 5 4
9 10 21
7 10 21
4 10 29
5 10 8
4 14 8
11 12 24
10 13 13
3 10 1
5 12 24
2 15 23
6 10 18
6 15 25

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# ダイクストラ法　優先度付きキュー　heapq w
# !! キューのタプルの順番に注意
# ---------------------------------------------------------------------------------------------------------

import heapq

# 入力
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

# 隣接リストの作成（重み付きグラフなので、各辺について (隣接頂点, 重み) のタプルを記録する）
G = [list() for i in range(N + 1)]
for a, b, c in edges:
    G[a].append((b, c))
    G[b].append((a, c))

# print(G)

# 配列・キューの初期化（キューには (距離, 頂点番号) のタプルを記録する）
# 距離が最短のものからheappopできるのでこの順のタプルにする
INF = 10**10
kakutei = [False] * (N + 1)
cur = [INF] * (N + 1)
cur[1] = 0
Q = []

heapq.heappush(Q, (cur[1], 1))

# print(Q)

# ダイクストラ法
while len(Q) >= 1:
    # 次に確定させるべき頂点を求める
    # （ここでは、優先度付きキュー Q の最小要素を取り除き、その要素の 2 番目の値（頂点番号）を pos に代入する）
    pos = heapq.heappop(Q)[1]

    # Q の最小要素が「既に確定した頂点」の場合
    if kakutei[pos] == True:
        continue

    # cur[x] の値を更新する
    kakutei[pos] = True
    for nex in G[pos]:
        # 書籍内のコードとは pos = e[0], cost = e[1] で対応している
        # 小さい値なら更新して
        if cur[nex[0]] > cur[pos] + nex[1]:
            cur[nex[0]] = cur[pos] + nex[1]
            heapq.heappush(Q, (cur[nex[0]], nex[0]))

    # print(pos, cur)

# 答えを出力
for i in range(1, N + 1):
    if cur[i] != INF:
        print(cur[i])
    else:
        print("-1")
