import io
import sys

_INPUT = """\
54 65


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

a, b = map(int, input().split())


def check(x):
    sum = 0
    for i in range(x):
        sum += i
    return sum


print(check(b - a) - a)
