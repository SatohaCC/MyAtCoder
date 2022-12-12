# A11 - Binary Search 1

import io
import sys


_INPUT = """\
10 800
10 20 30 40 50 60 70 80 90 100

"""
sys.stdin = io.StringIO(_INPUT)

# 二分探索を行うライブラリ
from bisect import bisect

N, X = map(int, input().split())
A = list(map(int, input().split()))


print(bisect(A, X))
# print("testt")
