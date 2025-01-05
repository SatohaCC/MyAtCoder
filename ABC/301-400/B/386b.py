import io
import sys

_INPUT = """\
1000000007
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

S = str(input())
count = len(S)

double_0 = 0

c = 0
for i in range(count):
    if c == 0 or c == 1:
        if S[i] == "0":
            c += 1
        else:
            c = 0
    if c == 2:
        double_0 += 1
        c = 0


print(count - double_0)
