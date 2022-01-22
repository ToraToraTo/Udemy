
# クラスメソッドとスタティックメソッドについて

"""
クラスメソッドはクラスをインスタンス化しなくてもアクセスする事ができる。（グローバル変数と近い）
クラスをインスタンス化せずにクラスオブジェクトのままで関数にアクセスするには、＠classmethodを関数の上に付けselfをclsに置き換える。
"""

class Person(object):

    # クラス変数
    kind = 'Human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

#     スタティックメソッド
    @staticmethod
    def about():
        print('About Human')

# クラスのインスタンス化
a = Person()

print(a.x)
print(a.what_is_your_kind())

# クラスオブジェクトのまま
b = Person
print(b.kind)
# クラスメソッドにアクセス
print(b.what_is_your_kind())

# スタティックメソッドの呼び出し
Person.about()