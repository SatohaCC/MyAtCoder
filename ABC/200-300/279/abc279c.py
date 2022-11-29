import io
import sys

_INPUT = """\
3 4
##.#
##..
#...
.###
..##
...#
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

H, W = map(int, input().split())

S = [[None] * H for i in range(W)]
T = [[None] * H for i in range(W)]


for i in range(H):
    s = input()
    for j in range(W):
        S[j][i] = s[j]

for i in range(H):
    s = input()
    for j in range(W):
        T[j][i] = s[j]

S.sort()
T.sort()

if S == T:
    print("Yes")
else:
    print("No")
