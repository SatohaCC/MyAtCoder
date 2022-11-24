import io
import sys

_INPUT = """\
10 6
1
5
2
9
6
9


"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------



n,q = map(int, input().split())

l = [i for i in range(0,n+1)]
idx = [i for i in range(0,n+1)]  # 各インデックスを保存

for i in range(q):
    x = int(input())
    j= idx[x]

    if j != n:
        right = l[j+1]  # 右側の数字

        l[j] ,l[j+1] = l[j+1],l[j]
        # 右側のインデックスとｘのインデックスを入れ返る
        idx[x] = j+1
        idx[right] = j

    else:  # 右端

        left = l[j-1]
        l[j] ,l[j-1] = l[j-1],l[j]
        idx[x] = j-1
        idx[left] = j
    print(idx)

print(*l[1:])