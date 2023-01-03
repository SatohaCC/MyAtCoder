import io
import sys

_INPUT = """\
5 4
1 2
1 3
1 4
1 5
2 3
2 4
1 3
5 1
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 辺の有無の判定
# ---------------------------------------------------------------------------------------------------------

# N = int(input())
# N, X, Y = map(int, input().split())
N, K = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]

G = [[0 for i in range(N)] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1][b - 1] = 1
    G[b - 1][a - 1] = 1

for i in range(K):
    a2, b2 = map(int, input().split())
    if G[a2 - 1][b2 - 1]:
        print("YES")
    else:
        print("NO")
