import io
import sys

_INPUT = """\
10 1

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
import math

a, b = map(int, input().split())


def calc(x):
    return 1 * b * x + a / math.sqrt(x + 1)


min = 0
for i in range(0, 10):
    print(calc(i))
