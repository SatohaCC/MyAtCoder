import io
import sys

_INPUT = """\
7
2 3
3 4
3 1
1 7
1 5
5 6
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 幅優先探索を用いて気の中心を求めます。
# 木の直径を利用して、木の中心を求めます。
# 木の直径とは、存在する２つのノード間の最大距離のことを指します。
# 木の直径はまず、任意の頂点を１つ選び（今回は頂点１）、
# そこからの全頂点への最短距離を幅優先探索やダイクストラ法を用いて求めます。
# 次に、求めた距離が最も遠い頂点からもう一度、全頂点への最短距離を求めます。これが、木の直径になります。
# 木の中心には次のような性質があります。
# 「ある頂点が木の中心であるならば、すべての頂点への距離は【(木の直径 / 2)以下】となる」。
# これを用いて条件を満たすものを木の中心として出力します。
# 最後に中心となる頂点をソートしましょう。
#
# ---------------------------------------------------------------------------------------------------------

from collections import deque


def bfs(pos: int) -> list:
    "幅優先探索をおこない、頂点 pos からの距離を求める"
    dist = [10000] * N
    dist[pos] = 0
    Q = deque([pos])

    while Q:
        v = Q.popleft()
        for nxt in g[v]:
            if dist[nxt] == 10000:
                dist[nxt] = dist[v] + 1
                Q.append(nxt)

    return dist


N = int(input())

# 隣接行列の作成・入力
g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

# 頂点 1 からの距離を求める
dist = bfs(0)


print(dist)
# 最も遠い頂点からもう一度幅優先探索を行う
max_dist = max(dist)
print(max_dist)


for i in range(N):
    if dist[i] == max_dist:
        # 木の直径を求める
        diameter = max(bfs(i))
        break

# ある頂点が木の中心であるならば、すべての頂点への距離は「(木の直径 / 2)以下」となる
center = []
for i in range(N):
    dist = bfs(i)
    check = True
    for j in range(N):
        if dist[j] > (diameter + 1) // 2:
            check = False
    if check:
        center.append(i + 1)

# 木の中心をソートして出力する
center.sort()
print(center)
for i in center:
    print(i)
