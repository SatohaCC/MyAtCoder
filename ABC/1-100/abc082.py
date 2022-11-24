import io
import sys

_INPUT = """\
ratcode
atlas


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

s = list(input())
t = list(input())

s = "".join(sorted(s))
t = "".join(sorted(t, reverse=True))


if s < t:
    print("Yes")
else:
    print("No")
