import io
import sys

_INPUT = """\
100
"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------
"""
問題文
整数 W が与えられます。
あなたは以下の条件をすべて満たすようにいくつかのおもりを用意することにしました。

おもりの個数は 1 個以上 300 個以下である。
おもりの重さは 10 6以下の正整数である。
1 以上 W 以下のすべての正整数は 良い整数 である。ここで、以下の条件を満たす正整数 n を良い整数と呼ぶ。
用意したおもりのうち 3 個以下 の異なるおもりを自由に選んで、選んだおもりの重さの和を n にすることができる。 　
条件を満たすようなおもりの組を 1 つ出力してください。

制約
1≤W≤10 6
W は整数
"""


w= int(input())

if w>=4:
    print(3)
    if w%2==0:
        print(w//2-1,w//2+1,1)
    else:
        print(w//2-1,w//2+1,1)
elif w==3:
    print(3)
    print(1,2,1)
elif w==2:
    print(2)
    print(1,1)
elif w==1:
    print(1)
    print(1)



