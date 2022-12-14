import io
import sys

_INPUT = """\
5
aaa 9
bbb 10
ccc 10
ddd 10
bbb 11


"""
sys.stdin = io.StringIO(_INPUT)



# ---------------------------------------------------------------------------------------------------------
"""
ポエムオンラインジャッジ (Poem Online Judge, 以下 POJ と表記) は提出された文字列に得点をつけるオンラインジャッジです。
POJ に N 回の提出がありました。早い方から i 番目の提出では文字列 Siが提出されて、得点は Tiでした。
(同じ文字列が複数回提出される場合もあります)

ただし、POJ では 同じ文字列を提出しても得点が等しいとは限らない のに注意してください。
N 回の提出のうち、その提出よりも早い提出であって文字列が一致するものが存在しないような提出を オリジナル であると呼びます。
また、オリジナルな提出の中で最も得点が高いものを 最優秀賞 と呼びます。
ただし、そのような提出が複数ある場合は、最も提出が早いものを最優秀賞とします。

最優秀賞は早い方から何番目の提出ですか？
"""

n = int(input())

d={}
tmp=-1
ans=-1

for i in range(n):
    s,t= input().split()
    if s not in d:
        d[s] = int(t)  
        if tmp <int(t):
            tmp = int(t)
            ans = i+1

print(ans)


"""
下記だと同じ数値が２つあった場合にあとからでてきたものが選ばれてします。
print(max(d.values())[1])
{'aaa': (9, 1), 'bbb': (10, 2), 'ccc': (10, 3), 'ddd': (10, 4)}
この場合は 'bbb': (10, 2)と'ddd': (10, 4)}が10で同じ値。
"""

"""
最初にACした書き方
for i in range(n):
    s,t= input().split()
    if s not in d:
        d[s] = int(t), i+1  # i番目に出現したことも記録していく。iが０から始まるので+1しておく

tmp=0
for i in d.values():
    if tmp < int(i[0]):
        tmp =int(i[0])
        ans = i[1]  
print(ans)
"""