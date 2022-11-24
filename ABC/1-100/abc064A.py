import io
import sys

_INPUT = """\
4 3 2


"""
sys.stdin = io.StringIO(_INPUT)


# ---------------------------------------------------------------------------------------------------------


# n = int(input())

# r, g, b = map(int, input().split())
a = int(input().replace(" ", ""))

if a % 4 == 0:
    print("YES")
else:
    print("NO")
