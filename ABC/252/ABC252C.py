import io
import sys

_INPUT = """\
5
0123456789
1245678903
1256789034
1234567890
0123456789

"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------
n=int(input())
s=[]
for i in range(n):
	s.append(input())
cnt=[[0 for j in range(10)]for i in range(10)]
print(cnt)

for i in range(n):
    for j in range(10):
        cnt[int(s[i][j])][j] += 1

print(cnt)
mx=[0 for i in range(10)]
for i in range(10):
	for j in range(10):
		mx[i]=max(mx[i], 10 * (cnt[i][j] - 1) + j)
print(min(mx))