import io
import sys

_INPUT = """\
toyotasystems
toyotasystems



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
s = input()
t = input()

if s.count(t):
    print("Yes")
else:
    print("No")
