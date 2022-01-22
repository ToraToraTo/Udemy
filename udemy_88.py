
# クラス変数について
"""
クラス内で固定されている値はクラス変数を用いる事で他のオブジェクトでも使用する事ができる。
その為、クラス変数を用いた場合は例２のようになり、クラスインスタンスを複数作り、それぞれからクラス変数のリストに対して値を入れると
他のインスタンスでも共有される。
その為、クラス変数を使う場合は全てのオブジェクトで使う値を入れておく時に使う。
もし、他のオブジェクトで共有されたくない場合は、イニシャライズの中に宣言して使う。
"""

class Person(object):

    # クラス変数
    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)



# クラスのインスタンス化
a = Person('A')
b = Person('B')



# インスタンス化したクラスのメソッドを実行
a.who_are_you()
b.who_are_you()


# 例２
class T(object):
    # words = []

    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)


# クラスのインスタンス化
c = T()
d = T()

# インスタンス化の関数を実行
c.add_word('add 1')
c.add_word('add 2')
print(c.words)

d.add_word('add 3')
d.add_word('add 4')
print(d.words)