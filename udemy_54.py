
# Docstringsについて
# 関数の説明については関数の中に記述する。

"""
一番最初にこの関数はどういった処理を行うものなのかを記述する。
次にArgsで引数の型が何でどういった事に使われているのかの説明を記述する。
最後にReturnsで、戻り値の型は何で、どういった結果が返ってくるのかを記述する。
"""

def example_func(param1, param2):
    """ Example function with types documented in the docstring.

    Args:
        param1 (int): The first parameter.
        param2 (int): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    """

    print(param1)
    print(param2)
    return True


# 関数名に__doc__をつける事で、関数内に記述されているドキュメントを表示する事ができる。
print(example_func.__doc__)