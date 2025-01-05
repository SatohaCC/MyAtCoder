import io
import sys

_INPUT = """\
frequency
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------

N = input()

abc = "abcdefghijklmnopqrstuvwxyz"
d = {}

for s in abc:
    d[s] = 0


def check_string(string, d):
    for i in range(len(string)):
        if string[i] in d:
            d[string[i]] += 1
    return d


def find_max_value(d):
    max_value = 0
    for key, value in d.items():
        if value > max_value:
            max_value = value

    return max_value


result = check_string(N, d)
max_value = find_max_value(result)

for i in range(len(abc)):
    if d[abc[i]] == max_value:
        print(abc[i])
        break
