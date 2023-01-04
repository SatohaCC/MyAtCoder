import io
import sys

_INPUT = """\
5 2 5
1 2
1 3
3 4
3 5
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# DFS
# 木　単純パス
# ---------------------------------------------------------------------------------------------------------

from collections import deque

N, X, Y = map(int, input().split())

G = [list() for i in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())

    G[a].append(b)
    G[b].append(a)


# 幅優先探索の初期化
# dist[i] = ? ではなく dist[i] = -1 で初期化していることに注意
dist = [-1] * (N + 1)
dist[X] = X
Q = deque()
Q.append(X)

# 幅優先探索
a = []

while len(Q) >= 1:
    pos = Q.popleft()
    for nex in G[pos]:
        # 未到達を到達にする
        if dist[nex] == -1:
            # 現在地を設定
            dist[nex] = pos
            Q.append(nex)

ans = []
while Y != dist[Y]:
    ans.append(Y)
    Y = dist[Y]
ans.append(Y)
print(*ans[::-1])
