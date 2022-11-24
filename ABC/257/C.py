import io
import sys

_INPUT = """\
5
10101
60 50 50 50 60



"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------


n = int(input())

s = input()

w = list(map(int, input().split()))

adult=[]
child=[]

for i in range(5):
    if s[i] =='1':
        adult.append(w[i])
    else:
        child.append(w[i])

print(adult)
print(child)
