import io
import sys

_INPUT = """\
3 4
1 2
2 1
2 3
3 2
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 弱連結な有向グラフにおいて、
#   ある頂点から始めてすべての辺を一筆書きして最初の頂点に戻ってくることができるための必要十分条件は以下のようになります。
# ・すべての頂点において、入次数と出次数が一致する。
# ---------------------------------------------------------------------------------------------------------

# N = int(input())
n, m = map(int, input().split())
# A, B = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]


G = [[0 for i in range(n)] for i in range(n)]

fromC = [0] * n

toC = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    # print(a, b)
    G[a - 1][b - 1] += 1


# print(fromC, toC)

# print(G)
for i in range(n):
    # print(G[i])
    for j in range(n):
        if G[j][i] > 0:
            fromC[i] += G[j][i]
        if G[i][j] > 0:
            toC[i] += G[i][j]


if fromC == toC:
    print(1)
else:
    print(0)


# for i in range(n):
#     # Ans.append(G[i])
#     # print(sum(G[i]))
#     if sum(G[i]) % 2 != 0:
#         Ans += 1


# if Ans in [0, 2]:
#     print(1)
# else:
#     print(0)

# # for i in range(n):
# #     for j in range(n):
# #         # print(G[i][j], G[j][i])
# #         if G[i][j] + G[j][i] > 1:
# #             a = [i + 1, j + 1]
# #             a.sort()
# #             if a not in Ans:
# #                 Ans.append(a)

# # print(*Ans)
# # # print(len(Ans))
# # for i in range(len(Ans)):
# #     print(Ans[i])
