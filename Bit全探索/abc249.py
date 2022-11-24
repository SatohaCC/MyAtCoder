import io
import sys

_INPUT = """\
4 2
abi
aef
bc
acg
"""
sys.stdin = io.StringIO(_INPUT)

N,K=map(int,input().split())

str_list=[]

for i in range(N):
    s = input()
    str_list.append(s)

ans=0

for bit in range(1<<N):
    ans_tmp=0
    choosed=[]
    for i in range(N):
        if bit>>i & 1:
            print(bin(bit))
            choosed.append(str_list[i])
    d={}
    for j in choosed:
        for k in j:
            if k not in d:
                d[k]=0
            d[k] +=1
    
    ans_tmp= list(d.values()).count(K)
    ans = max(ans,ans_tmp)

print(ans)