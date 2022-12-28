import io
import sys

_INPUT = """\
15 30
6 9
9 10
2 9
9 12
2 14
1 4
4 6
1 3
4 14
1 6
9 11
2 6
3 9
5 9
4 9
11 15
1 13
4 13
8 9
9 13
5 15
3 5
8 10
2 4
9 14
1 9
2 8
6 13
7 9
9 15


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 深さ優先探索　DFS
# Q:頂点数 N、辺数 M の連結なグラフが与えられます。
# このグラフについて、頂点 1 から頂点 N までの単純パスを一つ出力してください。
# ---------------------------------------------------------------------------------------------------------
import sys

sys.setrecursionlimit(1 << 20)
N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]
0
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


visited = [False for _ in range(N + 1)]
path = []

# print(G)


def dfs(pos: int):
    path.append(pos)

    # ゴール地点にたどり着いた！
    if pos == N:
        # 答えを出力して終了
        for x in path:
            print(x)
        exit(0)

    # その他の場合
    visited[pos] = True
    for j in G[pos]:
        if visited[j] == False:
            dfs(j)
    # print(path)
    path.pop()


dfs(1)
