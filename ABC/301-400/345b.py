import io
import sys

_INPUT = """\
123456789123456789

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------
import math
from decimal import ROUND_HALF_EVEN, ROUND_HALF_UP, Decimal

X = int(input())
print((X + 9) // 10)
