import io
import sys

_INPUT = """\
6
3 2
1 6
4 5
1 3
5 5
9 8

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

import numpy

N = int(input())

points = [list(map(int, input().split())) for _ in range(N)]


def calc(x1, y1, x2, y2):
    a = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2
    tmp = numpy.sqrt(a)
    return tmp


for i in range(N):
    max_point = []
    max_carry = -1

    for j in range(N):
        if i == j:
            continue
        if max_carry < calc(points[i][0], points[i][1], points[j][0], points[j][1]):
            max_carry = calc(points[i][0], points[i][1], points[j][0], points[j][1])
            max_point = j

    print(max_point + 1)
