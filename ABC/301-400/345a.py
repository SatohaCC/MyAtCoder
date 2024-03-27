import io
import sys

_INPUT = """\
==>
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

S = input()

r = False
l = False

if S[0] == "<" and S.count("<") == 1:
    r = True

if S[-1] == ">" and S.count(">") == 1:
    l = True

if r and l and S.count("=") >= 1:
    print("Yes")
else:
    print("No")
