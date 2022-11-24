import io
import sys
import math

_INPUT = """\
10000



"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())

def cal(s1,s2):
    str_len = max(len(str(s1)),len(str(s2)))
    return str_len

ans_tmp=N*N
ans_list=[]

a = int(N**0.5)
for i in range(1,a+1):
    if N%i==0:
        ans_list.append([i,int(N/i)])


for s in ans_list:
    ans_tmp= min(ans_tmp,cal(s[0],s[1]))

print(ans_tmp)

