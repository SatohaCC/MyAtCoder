import io
import sys

_INPUT = """\
1 2

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

a, b = map(int, input().split())

print(b, a)
