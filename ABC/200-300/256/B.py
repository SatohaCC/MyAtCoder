import io
import sys

_INPUT = """\
10
2 2 4 1 1 1 4 2 2 1


"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------
import copy

n = int(input())

a = list(map(int, input().split()))
b=[]
p=0

m=[0 for i in range(105)]

for i in range(n):
    m[0] = 1
    b = copy.deepcopy(m)
    for j in range(3,-1,-1):
        m[j+a[i]] ,m[j]= b[j] ,0
    
    for k in range(4,105):
        if m[k] ==1:
            p+=1
        m[k] = 0
print(p)

