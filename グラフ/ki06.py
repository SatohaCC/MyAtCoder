import io
import sys

_INPUT = """\
7
1 3
1 5
2 3
4 3
6 5
7 1
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 木の中で三角形を作る
# 　b を中心とする三角形の個数は 「b に接続する頂点からなる、相異なる 2 つの頂点のペアの数
# ---------------------------------------------------------------------------------------------------------

N = int(input())

g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

num_of_triangles = 0


print(g)
for i in range(N):
    num_of_triangles += len(g[i]) * (len(g[i]) - 1) // 2

if num_of_triangles % 2 == 0:
    print("erik")
else:
    print("paiza")
