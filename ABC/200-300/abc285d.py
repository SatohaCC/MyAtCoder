import io
import sys

_INPUT = """\
2
b m
m d


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

N = int(input())
S = []
T = []

# N, X, Y = map(int, input().split())
# s,t = map(int, input().split())
# A = list(map(int, input().split()))
num = []
for i in range(N):  # M
    a, b = input().split()
    num.append(a)
    num.append(b)
    S.append(a)
    T.append(b)

num2 = list(set(num))
n = len(num2)


G = [[0 for i in range(n)] for i in range(n)]
fromC = [0] * n

toC = [0] * n
for i in range(N):
    a = num2.index(S[i])
    b = num2.index(T[i])
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
    print("No")
else:
    print("Yes")
