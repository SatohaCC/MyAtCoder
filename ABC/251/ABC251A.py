import io
import sys

_INPUT = """\
zz



"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------


s = input()
ans = s*6

print(ans[:6])
