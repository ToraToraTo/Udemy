
# 関数内関数について

"""
関数内にさらに関数を定義する。
InnerFunctionはその関数の中でしか使用しない関数を定義する時に使用する。

"""


def outer(a, b):

    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)

outer(1, 2)