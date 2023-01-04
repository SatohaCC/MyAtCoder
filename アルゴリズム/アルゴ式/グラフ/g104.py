import io
import sys

_INPUT = """\
6 7 0
0 1
0 5
1 3
1 5
2 3
3 4
4 5
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 友達の友達の人数　セット
#
# ---------------------------------------------------------------------------------------------------------
# N = int(input())
N, M, X = map(int, input().split())
# A, B = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]

G = [[] for _ in range(N)]
for i in range(M):  # M
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# print(G[X])
# リストのままだとだめ
friends = set(G[X])
ans = set()
for i in G[X]:
    # print(G[i])
    for j in G[i]:
        # print(j)
        if j != X and j not in friends:
            ans.add(j)
print(len(ans))
