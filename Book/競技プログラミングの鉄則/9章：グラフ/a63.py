import io
import sys

_INPUT = """\
6 6
1 4
2 3
3 4
5 6
1 2
2 4

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 幅優先探索　重みなし無向グラフ　最短経路問題　キュー
# 頂点 1 から頂点 k まで、辺を何本かたどって移動することを考えるとき、
# たどるべき辺の本数の最小値を出力せよ。
# ただし、移動不可能な場合は −1 を出力せよ。
# ---------------------------------------------------------------------------------------------------------


from collections import deque

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# 隣接リストの作成
G = [list() for i in range(N + 1)]

for a, b in edges:
    G[a].append(b)
    G[b].append(a)

print(G)

# 幅優先探索の初期化
# dist[i] = ? ではなく dist[i] = -1 で初期化していることに注意
dist = [-1] * (N + 1)
dist[1] = 0
Q = deque()
Q.append(1)

# 幅優先探索
while len(Q) >= 1:
    pos = Q.popleft()
    for nex in G[pos]:
        # 未到達を到達にする
        if dist[nex] == -1:
            # 現在地+1の距離を設定
            dist[nex] = dist[pos] + 1
            Q.append(nex)

# 頂点 1 から各頂点までの最短距離を出力
for i in range(1, N + 1):
    print(dist[i])
