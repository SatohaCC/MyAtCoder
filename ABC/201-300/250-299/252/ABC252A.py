import io
import sys

_INPUT = """\
97
"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------


num = int(input())
abc = "abcdefghijklmnopqrstuvwxyz"
print(abc[num-97])
