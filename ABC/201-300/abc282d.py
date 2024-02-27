import io
import sys

_INPUT = """\
5 4
4 2
3 1
5 2
3 2

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

import queue

# N  * (N - 1) // 2
def com(N):
    return N * (N - 1) // 2


# 色
WHITE, BLACK = 0, 1

# 入力
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
G = [[] for _ in range(N)]
for e in edges:
    u, v = e[0] - 1, e[1] - 1
    G[u].append(v)
    G[v].append(u)

# 各変数
num_ng_edges = 0
is_bipartite = True
color = [-1] * N

# 各連結成分を走査する
for s in range(N):
    if color[s] != -1:
        continue

    # 白色頂点、黒色頂点の個数
    white_num, black_num = 0, 0

    # 頂点 s を始点とする BFS
    que = queue.Queue()
    que.put(s)
    color[s] = WHITE
    while not que.empty():
        v = que.get()

        # 頂点の個数をカウント
        if color[v] == WHITE:
            white_num += 1
        else:
            black_num += 1

        # 頂点 v の隣接頂点について
        for v2 in G[v]:
            if color[v2] != -1:
                # すでに色が塗られているとき
                if color[v2] == color[v]:
                    # 隣接頂点が同色はダメ
                    is_bipartite = False
            else:
                # 新しい頂点を処理
                color[v2] = 1 - color[v]
                que.put(v2)

    # ng 辺の本数
    num_ng_edges += com(white_num) + com(black_num)

# 答え
print(com(N) - M - num_ng_edges if is_bipartite else 0)
