
# クラスの定義について

"""
class クラス名(object):
でクラスの定義は出来ます。(object)は無くても大丈夫だが、コードスタイルの暗黙の了解で記述する。
Python3からは無くても大丈夫になったので、他のコードでは無い場合もある。

コンストラクタ
クラス関数で__init__(self)はそのクラスのオブジェクトを作成した時に自動的に実行される。
__init__(self, 変数名)
とする事で、作成したクラスオブジェクト内で値を保持する事ができる。
クラスオブジェクト作成時にセットした値はクラスオブジェクト内で保持されるので、クラス内の関数でも使う事ができる。
その際は、値を保持している変数名の前に　self.変数名　というようにして呼び出す。

クラス内関数の中で同じクラス内の関数は　self.　を付ける事で呼び出す事もできる。
クラス内関数に引数を持たせる場合、宣言時はselfが必要だが、同じクラス内でその関数を呼び出して引数を渡す際はselfは必要ない。

デストラクタ
クラスオブジェクトが終了する時に呼ばれるメソッド
def __del__(self):
このデストラクタはクラスオブジェクトが使われなくなった時に呼び出されて実行される。
もし、任意の場所で明示的にこのデストラクタを呼び出して使う場合は、del クラスオブジェクト名　として実行する。

"""

class Person(object):

    def __init__(self, name):
        self.name = name

    def say_something(self):
        print('I m {} Hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('Run' * num)

    def __del__(self):
        print('Good dye')



# クラスのオブジェクトを作成する
person = Person('Maik')
person.say_something()

# 明示的にデストラクタを実行する。
del person