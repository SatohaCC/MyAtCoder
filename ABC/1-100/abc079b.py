import io
import sys

_INPUT = """\
86
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# https://atcoder.jp/contests/abc079/tasks/abc079_b
#
# ---------------------------------------------------------------------------------------------------------

N = int(input())

numbers = [0] * 87
numbers[0] = 2
numbers[1] = 1

for i in range(2, 86 + 1):
    numbers[i] = numbers[i - 2] + numbers[i - 1]

print(numbers[N])
