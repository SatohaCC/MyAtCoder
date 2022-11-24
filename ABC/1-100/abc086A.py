import io
import sys

_INPUT = """\
1 21

"""
sys.stdin = io.StringIO(_INPUT)


# ---------------------------------------------------------------------------------------------------------


# n = int(input())

a, b = map(int, input().split())

# a = list(map(int, input().split()))

a, b = map(int, input().split())
if a * b % 2 == 0:
    print("Even")
else:
    print("Odd")
