import io
import sys

_INPUT = """\
30



"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------


n = int(input())
print(2**n)

