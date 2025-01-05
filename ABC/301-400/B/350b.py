import io
import sys

_INPUT = """\
9 20
9 5 1 2 2 2 8 9 2 1 6 2 6 5 8 7 8 5 9 8
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# https://qiita.com/hyouchun/items/c2a4aa2b5ff2c177f120#%E5%95%8F%E9%A1%8C-2
#
# ---------------------------------------------------------------------------------------------------------
N, Q = map(int, input().split())

T = list(map(int, input().split()))
ans = []
for i in range(Q):
    if T[i] not in ans:
        ans.append(T[i])
    else:
        ans.remove(T[i])


print(N - len(ans))
