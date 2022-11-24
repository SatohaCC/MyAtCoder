
from bisect import bisect_left, bisect_right
from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
print(A)
print()

indexes = defaultdict(list)
for i, x in enumerate(A):
    indexes[x].append(i)
    
# defaultdictでのindexに対して二分探索が使える
# 配列の中にLからRの数は何個あるか求めればよくなる

print(indexes)
print("1があるindexが帰ってくる",indexes[1])
print("ここから左と右で絞り込む")

print(bisect_right(indexes[1], 0))
print()
# bisect.bisect_left(a, x, lo=0, h=len(a))
# bisect_leftはソートされたリストaに対して順序を保ったままxを挿入できる箇所を探索します。
# leftが示す通り、aにすでにxが存在している場合は、挿入箇所は既存のxよりも左側になります。
# また、lo, hiを指定することで探索範囲を絞り込むことも可能です。デフォルトはaの全体が探索対象です。

for i in range(max(A)+1):
    print(i,indexes[i])

print()

q = int(input())

for _ in range(q):
    l, r, x = map(int, input().split())
    # indexと添字がずれるので-1して調節する
    l -= 1
    r -= 1
    print("x",x ,'は左',l,'から右',r,'までに',bisect_right(indexes[x], r) - bisect_left(indexes[x], l))
    print(" 　対象",x,indexes[x],"    left",l, '------------- ',bisect_left(indexes[x], l))
    print(" 　対象",x,indexes[x],"    right",r, '------------ ',bisect_right(indexes[x], r))
    res = bisect_right(indexes[x], r) - bisect_left(indexes[x], l)
    print()