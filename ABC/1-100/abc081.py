import io
import sys

_INPUT = """\
101
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

n = input()

print(n.count("1"))
