
# クロージャーについて

"""
以下の例ではInnerFunctionが定義されているが、最終的な戻り値はInnerFunctionが実行されるのではなく（（）がない状態）、InnerFunctionのオブジェクトが返されている。
そのため、outer()の戻り値はInnerFunctionのオブジェクトであり、値はセットされているがまだ実行されていない状態にある。
InnerFunctionを実行するには、outer()の戻り値を代入している変数に（）をつけて関数として実行し、その戻り値を変数に代入する事でInnerFunctionが実行され結果が返される。

このクロージャーは値を渡すけど、処理自体は他の処理を行った後に実行したい場合に使用する。（一時的に処理を待つ）
"""

def outer(a, b):

    def inner():
        return a + b

    return inner

f = outer(1, 2)
r = f()
print(r)



def circle_area_func(pi):

    def circle_area(radius):
        return pi * radius * radius

    return circle_area

# 最初に円周率を決めて、その円周率が設定されている関数をca1,ca2 に代入。
ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

# 実際にそれぞれのInnerFunctionに引数を渡す事ではじめて関数が実行される。
print(ca1(10))
print(ca2(10))

