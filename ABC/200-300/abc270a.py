import io
import sys

_INPUT = """\
1 2
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# bit演算
# https://atcoder.jp/contests/abc270/editorial/4877
# ---------------------------------------------------------------------------------------------------------

a, b = map(int, input().split())
print(a | b)