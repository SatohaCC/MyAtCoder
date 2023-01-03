import io
import sys

_INPUT = """\
3 2
1 2
1 3
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
# 弱連結な有向グラフにおいて、すべての辺を一筆書きすることができるための必要十分条件は以下のいずれかを満たすことです。

# ・すべての頂点において、入次数と出次数が一致する。
# ・以下の条件をすべて満たす。
# ・(入次数) = (出次数 + 1) となる頂点がちょうど 1 つ存在する。
# ・(入次数 + 1) = (出次数) となる頂点がちょうど 1 つ存在する。
# ・残りのすべての頂点について、入次数と出次数が一致する。
#
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


# print(G)
for i in range(n):
    # print(G[i])
    for j in range(n):
        if G[j][i] > 0:
            fromC[i] += G[j][i]
        if G[i][j] > 0:
            toC[i] += G[i][j]


# ・すべての頂点において、入次数と出次数が一致する。
if fromC == toC:
    print(1)
    exit()

# または、
# ・以下の条件をすべて満たす。
# ・(入次数) = (出次数 + 1) となる頂点がちょうど 1 つ存在する。factorA
# ・(入次数 + 1) = (出次数) となる頂点がちょうど 1 つ存在する。factorB
# ・残りのすべての頂点について、入次数と出次数が一致する。factorC

factorA = False
factorB = False
factorC = False

countA = []
countB = []
countC = []
for i in range(n):
    # print(fromC[i], toC[i])
    if fromC[i] == toC[i] + 1:
        countA.append(i)
    if fromC[i] + 1 == toC[i]:
        countB.append(i)
    if fromC[i] == toC[i]:
        countC.append(i)

if len(countA) == 1 and len(countB) == 1 and len(countC) == n - 2:
    print(1)
else:
    print(0)
