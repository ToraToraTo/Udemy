
# 独自例外の作成について

"""
:raise エラーメッセージを自分で作成して表示する。
オリジナルのExceptionを作成するにはクラスを作成して、Exceptionクラスを継承する。
これにより、Exceptionの時に自分で作成したExceptionクラス名で例外処理を行う事ができる。
"""

class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']

    for word in words:
        if word.isupper():
            raise UppercaseError(word)


try:
    check()
except UppercaseError as ex:
    print("this is my fault.Go next")