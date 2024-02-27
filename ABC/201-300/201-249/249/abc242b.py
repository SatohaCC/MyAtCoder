import io
import sys

_INPUT = """\
abad


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 辞書順で最小
# abc
# ---------------------------------------------------------------------------------------------------------

s = input()
lis = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

for i in lis:
    print(i * s.count(i), end="")


#####################################
print()
l = []
for i in range(ord("a"), ord("z") + 1):
    c = chr(i)
    l.append(s.count(c))
t = ""
for i in range(26):
    t += chr(ord("a") + i) * l[i]
print(t)
