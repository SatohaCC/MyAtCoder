import io
import sys

_INPUT = """\
8 18
0 2
6 7
1 7
0 4
2 5
1 3
3 4
4 7
0 5
0 3
1 4
2 4
2 6
2 7
2 3
5 6
0 1
3 5

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------


N, M = map(int, input().split())

G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

ans_i = 0
for i in range(N):
    G[i].sort()
    if len(G[i]) > len(G[ans_i]):
        ans_i = i
print(*G[ans_i])
