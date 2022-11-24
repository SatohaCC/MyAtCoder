import io
import sys

_INPUT = """\
2017/01/07

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

s = input()

print("2018" + s[4:])


# スライスは遅い？
y, m, d = input().split("/")

new_y = str(int(y) + 1)

print(new_y, m, d, sep="/")
