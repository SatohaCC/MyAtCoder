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

# N = int(input())
N, M = map(int, input().split())

G = [[0 for _ in range(N)] for _ in range(N)]

for i in range(M):  # M
    a, b = map(int, input().split())
    G[a - 1][b - 1] += 1
    G[b - 1][a - 1] += 1

print(G)
