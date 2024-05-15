import io
import sys

_INPUT = """\
aaaa
bbbbaaaa

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# B - Typing
#
# ---------------------------------------------------------------------------------------------------------

S = input()
T = input()

L = []

j = 0

for i in range(len(S)):
    while S[i] != T[j]:
        j += 1
    L.append(j + 1)
    j += 1
print(*L)
