import io
import sys

_INPUT = """\
4 3
1 3
4 2
3 2

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

n, m = map(int, input().split())
sum = [0 for _ in range(n)]

c1 = 0
c2 = 0
c3 = 0
import sys

sys.setrecursionlimit(120000)
ans = []
# 深さ優先探索を行う関数
# pos は現在位置、visited[x] は頂点 x が青色かどうかを表す真偽値
def dfs(pos, G, visited):
    ans.append(pos)
    # 頂点nexに進むときはdfsを再帰呼び出し
    visited[pos] = True
    # print("現在位置：", pos)
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)
        # print(i, visited)


# 隣接リストの作成 0は空にしておく
G = [[] for _ in range(n)]


for i in range(m):  # M
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

    sum[a - 1] += 1
    sum[b - 1] += 1
visited = [False] * (n)
dfs(0, G, visited)

# 連結かどうかの判定（answer = True のとき連結）
answer = True
for i in range(n):
    if visited[i] == False:
        answer = False
        break


for i in range(n):
    # print(sum[i])
    if sum[i] == 1:
        c1 += 1
    elif sum[i] == 2:
        c2 += 1
    elif sum[i] > 2:
        c3 += 1


if (c1 == 2) and (c3 == 0) and c2 == (n - 2) and (n - m) == 1 and answer:
    print("Yes")
else:
    print("No")
