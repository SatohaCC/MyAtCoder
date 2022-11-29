import io
import sys

_INPUT = """\
v


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

s = input()

v = s.count("v")
w = s.count("w")

print(v + w * 2)
