import io
import sys

_INPUT = """\
abracadabra
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# https://qiita.com/hyouchun/items/c2a4aa2b5ff2c177f120#%E5%95%8F%E9%A1%8C-2
#
# ---------------------------------------------------------------------------------------------------------


S = input()


def list_substrings(word):
    substrings = []
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            substrings.append(word[i:j])
    return substrings


# 例

substrings = list_substrings(S)
print(len(set(substrings)))

