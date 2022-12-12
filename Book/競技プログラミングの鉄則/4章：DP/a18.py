import io
import sys

_INPUT = """\
3 7
2 2 3

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# 部分和問題　DP
# いくつか選んで合計がSになる方法は存在するか
# ---------------------------------------------------------------------------------------------------------

N, S = map(int, input().split())
A = list(map(int, input().split()))


dp = [[False for _ in range(S + 1)] for _ in range(N + 1)]

# i=0 はカードを選んでいない状態なのでj=0が０になり、Trueとなる
# dp[2][3]はカード２まで選んだ状態で合計値が３になる場合があるなら、True
dp[0][0] = True


for i in range(1, N + 1):
    for j in range(S + 1):

        # カードi-1の時点の合計がjであり、カードiを選ばない
        # dp表の縦の動きのみ
        print(j, A[i - 1])
        if j < A[i - 1]:
            if dp[i - 1][j]:
                dp[i][j] = True
                print("True")
        
        # カードi-1の時点の合計がjであり、カードiを選ばない
        # カードi-1の時点で合計がj-A[i]であり、カードiを選ぶ。
        if j >= A[i - 1]:
            if dp[i - 1][j] or dp[i - 1][j - A[i - 1]]:
                dp[i][j] = True
                print("True2")
    print()

if dp[N][S]:
    print("Yes")
else:
    print("No")
