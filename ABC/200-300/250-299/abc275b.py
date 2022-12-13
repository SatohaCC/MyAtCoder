import io
import sys

_INPUT = """\
5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 隣接リスト
#
# ---------------------------------------------------------------------------------------------------------

N, M = map(int, input().split())
A = [0 for i in range(M)]
B = [0 for i in range(M)]

for i in range(M):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

g = [list() for i in range(N + 1)]

for i in range(M):
    g[A[i]].append(B[i])
    g[B[i]].append(A[i])

for i in range(1, N + 1):
    g[i].sort()
    print(len(g[i]), *g[i])
