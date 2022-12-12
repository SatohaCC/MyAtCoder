import io
import sys

_INPUT = """\
5 4
1 2
2 3
3 4
3 5

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# グラフ　隣接リスト表現
#
# ---------------------------------------------------------------------------------------------------------

N, M = map(int, input().split())

g = [[] for i in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    g[A].append(B)
    g[B].append(A)


for i in range(1, N + 1):
    s = str(i)
    s += ": {"
    s += ", ".join(map(str, g[i]))
    s += "}"
    print(s)
