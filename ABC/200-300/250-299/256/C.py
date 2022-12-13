import io
import sys

_INPUT = """\
5 13 10 6 13 9




"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------


h1,h2,h3,w1,w2,w3 = map(int, input().split())

hlist = [h1,h2,h3]
wlist = [w1,w2,w3]
h_tmp=[[]for i in range(31)]

list = [i for i in range(1,31)]

for k in hlist:
    for i in list:
        for j in list:
            if i+j <k:
                h_tmp[k].append([i,j,k-i-j])
