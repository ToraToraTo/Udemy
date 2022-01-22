
# クラス多重継承について

"""
複数のクラスの機能を継承する多重継承。
継承するクラスの両方に同じ名前の関数がある場合、先に継承させたクラスメソッドが呼ばれるので注意。
呼んで欲しいメソッドがあるクラスを先に継承させる。
ただし、多重継承は後々バグに繋がる可能性があるので使わないのが望ましい。
"""

class Person(object):
    def talk(self):
        print('Talk')

    def run(self):
        print('Person Run')

class Car(object):
    def run(self):
        print('Car Run')


# 二つのクラスの機能を継承したクラス
class PersonCarRobot(Car, Person):
    def fly(self):
        print('Fly')


# クラスのインスタンス化
personCarRobot = PersonCarRobot()



# インスタンス化したクラスのメソッドを実行
personCarRobot.talk()
personCarRobot.run()
personCarRobot.fly()