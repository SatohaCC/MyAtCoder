import io
import sys

_INPUT = """\
ion

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
s = input()

count = len(s)
print(s[0] + str(count - 2) + s[-1])

# 別海
S = input()
c = len(S) - 2
print(S[0], c, S[-1], sep="")
