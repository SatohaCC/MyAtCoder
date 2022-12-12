import io
import sys

_INPUT = """\
45
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

N = int(input())

pare = 0
one = 0
baby = 1


for i in range(1, N + 1):
    pare += one

    one = 0
    one += baby

    baby = 0
    baby += pare

    # print(i, ":  pare", pare, "  one", one, "  now", now, sep="")

print(pare + one + baby)
