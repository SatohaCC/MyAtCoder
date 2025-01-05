import io
import sys

_INPUT = """\
5
0 0 0 1 2
"""
sys.stdin = io.StringIO(_INPUT)


import math
from collections import deque

N = int(input())
B = list(map(int, input().split()))
A = deque()


def action_always(A, i):
    A.append(B[i])


def action_A(stack):
    return len(stack) <= 1


def action_B(stack):
    return 2 ** stack[-2] != 2 ** stack[-1]


def action_C(stack):
    if stack[-2] == stack[-1]:
        tmp1 = stack.pop()
        tmp2 = stack.pop()
        sum_tmp = 2**tmp1 + 2**tmp2
        x = int(math.log(sum_tmp, 2))
        stack.append(x)
        return True
    return False


for i in range(N):
    action_always(A, i)
    while len(A) > 1 and A[-2] == A[-1]:
        action_C(A)
print(len(A))
