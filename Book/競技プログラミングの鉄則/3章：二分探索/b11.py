# B11 - Binary Search 2
# sortするか考えるパターン
import io
import sys


_INPUT = """\
5
1 3 3 3 1
2
4
3
"""
sys.stdin = io.StringIO(_INPUT)

# 二分探索を行うライブラリ
from bisect import bisect

N = int(input())
A = list(map(int, input().split()))

# sort
A.sort()

Q = int(input())

# bisect([1, 1, 3, 3, 3], 3)を入れると5になるので
# X-1するのを忘れないように。

for i in range(Q):
    X = int(input())
    print(bisect(A, X - 1))
