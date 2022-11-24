import io
import sys

_INPUT = """\
2 10
1 3

"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------

n,w = map(int, input().split())
a = list(map(int, input().split()))


# セットを使うと重複を無視できる
ans=set()

for i in range(n):
    if a[i]<=w:
        ans.add(a[i])
    for j in range(i+1,n):
        if a[i]+a[j]<=w:
            ans.add(a[i]+a[j])
        for k in range(j+1,n):
            if a[i]+a[j]+a[k]<=w:
                ans.add(a[i]+a[j]+a[k])


print(len(ans))