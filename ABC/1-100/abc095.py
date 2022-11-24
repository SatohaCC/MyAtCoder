import io
import sys

_INPUT = """\
oxo

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

n = input()
count = 0
for i in n:
    if i == "o":
        count += 1
print(700 + 100 * count)
