import io
import sys

_INPUT = """\
6 6
1 2
1 3
2 4
3 4
4 5
4 6

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 深さ優先探索　DFS
#
# ---------------------------------------------------------------------------------------------------------


# 再帰呼び出しの深さの上限を 120000 に設定
import sys

sys.setrecursionlimit(120000)

# 深さ優先探索を行う関数
# pos は現在位置、visited[x] は頂点 x が青色かどうかを表す真偽値
def dfs(pos, G, visited):
    # 頂点nexに進むときはdfsを再帰呼び出し
    visited[pos] = True
    print("現在位置：", pos)
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)
        print(i, visited)


n, m = map(int, input().split())

# 隣接リストの作成 0は空にしておく
G = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

print(G)

# 深さ優先探索
visited = [False] * (n + 1)
dfs(1, G, visited)

# 連結かどうかの判定（answer = True のとき連結）
answer = True
for i in range(1, n + 1):
    if visited[i] == False:
        answer = False
        break

# 答えの出力
if answer == True:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
