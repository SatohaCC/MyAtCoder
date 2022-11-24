import io
import sys

_INPUT = """\
10

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
import itertools
N = int(input())
# 1と-1の全パターンで、（→）の順でセットになるのでプラスマイナスゼロになる
tt=[1,-1]
d= list(itertools.product(tt,repeat=N))

for i in d:
    c=0
    for j in i:
        c +=j
        if c<0:
            break
    if c ==0:
        for a in i:
            if a ==1:
                print('(',end='')
            else:
                print(')',end='')
        print()



