import io
import sys

_INPUT = """\
2 12



"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------



n,x =  map(int, input().split())

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
abc2 = []
for i in abc:
    for j in range(n):
        abc2.append(i)

print(abc2[x-1])
