import io
import sys

_INPUT = """\
4 4
0 3
0 2
1 2
3 1
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

# N = int(input())
N, M = map(int, input().split())
# A, B = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]

G = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)

for i in range(N):
    a = G[i]
    a.sort()
    print(*a)
