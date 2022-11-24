import io
import sys

_INPUT = """\
9
1 2 1 2 1 2 1 2 1
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

N = int(input())
A = list(map(int,input().split()))

pl = 0  # プラスが１ マイナスが-1
count = 1  #グラフで考えたときの頂点を数える。
for i in range(1, N):
    if A[i-1] - A[i] ==0: # プラマイ０は無視
        continue

    if pl== 0: # 初回、傾きが変わったタイミング
        if A[i-1] < A[i]: 
            pl=1
        else:
            pl=-1
        #print("pl==0:",A[i])

    elif pl!=0:

        if pl == -1: #減少中に
            if A[i-1] < A[i] : # 増加
                count +=1
                pl=0
        if pl == 1: #
            if A[i-1] > A[i] : # 
                #print(pl,A[i-1],A[i])
                count +=1
                pl=0
    

print(count) 
