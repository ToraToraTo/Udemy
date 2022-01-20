
# デコレーターについて

"""
以下のデコレーターでは引数のfuncにadd_numという関数のオブジェクトが代入されている。
次にInnerFunctionが実行され、「start」が表示される。
次に変数resultに引数funcが入るが、このfuncはadd_numであるので、add_numを呼び出した際に渡した引数がそのまま処理され結果がresultに代入される。
次に「end」が表示され、最後にresultを戻り値として返す。

デコレーターは「何かを包み込む」というイメージ。
"""

def print_moer(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper


def print_info(func):
    def wrapper(*args, **kwargs):
        print("start")
        # funcはadd_numが引数をセットされた状態で入ってくるのでそのままadd_numの処理が実行される。
        result = func(*args, **kwargs)
        print("end")
        return result

    return wrapper


# デコレーターをセットしたい関数の上で＠をつけてデコレーター関数名を記述する事で、デコレーターを実行する事ができる。
# 以下のようにデコレーターを複数付ける事も可能だが、順番を間違えると結果も異なるので注意が必要。

@print_info
@print_moer
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)


