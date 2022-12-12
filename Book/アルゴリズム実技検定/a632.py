import io
import sys

_INPUT = """\
4 5
s####
....#
#####
#...g
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# DFS https://atcoder.jp/contests/atc001/tasks/dfs_a
#
# ---------------------------------------------------------------------------------------------------------

import sys

sys.setrecursionlimit(1000000)

N = 5

visited = [False for _ in range(N)]


print(visited)


def dfs(i):
    visited[i] = True
    for j in E9[i]:
        if visited[j] == False:
            dfs(j)


dfs(5)
