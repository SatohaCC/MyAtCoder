import io
import sys

_INPUT = """\
2763
0
"""
sys.stdin = io.StringIO(_INPUT)


# ---------------------------------------------------------------------------------------------------------


N = int(input())
A = int(input())

# remainder
r = N % 500

if r <= A:
    print("Yes")
else:
    print("No")
