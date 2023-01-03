import io
import sys

_INPUT = """\
3 4
1 2
1 2
2 3
2 3
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 準オイラーグラフ (すべての辺を一筆書きすることができるかどうか判定してください。
# ただし、この問題では最終的に初めの頂点に戻らなくても良いものとします。
# なお、そのようなことが可能なグラフを準オイラーグラフといいます。)
# 連結な無向グラフにおいて、
# すべての辺を一筆書きすることができるための必要十分条件は以下のようになります。
# 次数が奇数である頂点の個数が、ちょうど 0 または 2 である。
# ---------------------------------------------------------------------------------------------------------

# N = int(input())
n, m = map(int, input().split())
# A, B = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for _ in range(N)]


G = [[0 for i in range(n)] for i in range(n)]


for i in range(m):
    a, b = map(int, input().split())
    # print(a, b)
    G[a - 1][b - 1] += 1
    G[b - 1][a - 1] += 1


Ans = 0

for i in range(n):
    # Ans.append(G[i])
    # print(sum(G[i]))
    if sum(G[i]) % 2 != 0:
        Ans += 1


if Ans in [0, 2]:
    print(1)
else:
    print(0)

# for i in range(n):
#     for j in range(n):
#         # print(G[i][j], G[j][i])
#         if G[i][j] + G[j][i] > 1:
#             a = [i + 1, j + 1]
#             a.sort()
#             if a not in Ans:
#                 Ans.append(a)

# print(*Ans)
# # print(len(Ans))
# for i in range(len(Ans)):
#     print(Ans[i])
