import io
import sys

_INPUT = """\
A
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

N = int(input())
N, X, Y = map(int, input().split())
A, B = map(int, input().split())
A = list(map(int, input().split()))
