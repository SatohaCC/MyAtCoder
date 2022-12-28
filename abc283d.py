import io
import sys

_INPUT = """\
(a(ba))


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
#
#
# ---------------------------------------------------------------------------------------------------------
S = input()
abcd = "abcdefghijklmnopqrstuvwxyz"
from collections import defaultdict


def check(string, i):
    j = 10000
    dict = defaultdict(list)

    for i in range(len(string[: i + 1])):
        if string[i] == "(":
            dict["("].append(i)
        elif string[i] == ")":
            dict[")"].append(i)

    if len(dict["("]) == len(dict[")"]):
        j = dict["("][0] + 1

    elif len(dict["("]) > len(dict[")"]):
        j = dict["("][-len(dict[")"])] + 1
    return j


ball = ()

for i in range(len(S)):

    if S[i] == "(":
        pass

    elif S[i] == ")":
        j = check(S, i)

        for q in range(j, i + 1):
            
            

    else:

        if S[i] not in ball:
            ball[S[i]] = 0

        if ball[S[i]] == 0:
            ball[S[i]] = i + 1
        else:
            print("No")
            exit()

print("Yes")
