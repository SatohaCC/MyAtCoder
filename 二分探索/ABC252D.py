import io
import sys

_INPUT = """\
15
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
"""
https://atcoder.jp/contests/abc252/tasks/abc252_d

"""

from bisect import bisect_left, bisect_right

n = int(input())
a = sorted(list(map(int, input().split())))

ans=0
for i in a:
    ans += bisect_left(a, i) * (n - bisect_right(a, i))
print(ans)