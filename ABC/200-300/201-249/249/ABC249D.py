import io
import sys

_INPUT = """\
10
1 3 2 4 6 8 2 2 3 7


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

N =int(input())
A = list(map(int,input().split()))

ans=0
c=0
max_a = max(A)
count = [0] * (max_a + 1)   # count[i]：数値 i の個数
for i in A:
    count[i] += 1

print(count)

for n1 in range(1, max_a+1):    # 1 ≦ N1 ≦ M
    nn = n1 * n1                # N1 * N1 で等式が成立する個数を考える
    if nn > max_a:              # 等式を満たす範囲は，1 ≦ N1 ≦ √M
        break
    c1 = count[n1]
    if c1 == 0:                 # N1が{Ai}中に存在しないなら以降はスキップ
        continue
    # N1*N1が{Ai}中に存在しないとき count[nn]=0となるため，存在する／しないの場合分け不要
    ans += (c1 * c1 * count[nn])
    for n2 in range(n1+1, max_a+1): # N1 < N2 ≦ M
        nn = n1 * n2
        if nn > max_a:
            break
        ans += (2 * c1 * count[n2] * count[nn]) # 上と同様，存在性の場合分け不要
print(ans)
 