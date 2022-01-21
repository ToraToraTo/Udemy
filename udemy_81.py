
# クラスの継承について

"""
クラスの継承ではベースとなる機能をもつクラスを作成し、オプションの機能を持つクラスでベースクラスの機能を継承する事で両方のクラスの機能を使う事ができる。
以下の例ではCarクラスは車としての走る機能であるベース機能のみを持っている。
次にToyotaCarクラスはクラス内に独自の機能は持っていないが、ベースとなる走る機能はCarクラスから継承されているので走る機能が使える。
更にTeslaCarクラスではベースとなる走る機能と独自で持つ自動運転機能のauto_runの両方を使う事ができる。

メソッドのオーバーライドについて
親クラスの持つメソッドと同じ名前で子クラスでも定義し、中身を書き換える事をオーバーライドという。

親クラスにコンストラクタを設定し、子クラスをインスタンス化する際に引数を渡すと親クラスのクラス変数を子クラスでも使う事ができる。
子クラスにコントラクタを記述する場合、親クラスのコンストラクタが先に実行されるので、その情報を上書きする。
super().__init__(上書きしたい子クラスのコンストラクタ変数)
として上書きを行う。
そして、親クラスにはないコンストラクタ変数はこれまでのコンストラクタと同様に、self.変数名に代入して使う。

プロパティについて
クラスをインスタンス化した後に、インスタンスからクラス変数の中身を書き換えられたくない時に使う。
クラス変数を宣言（self.クラス名）の時に、クラス変数名の前に _ を付けて宣言する。
また、クラス変数を外から完全にアクセス不能にする場合は __ とする事で外からのアクセスは出来なくなる。

そしてプロパティを設定するには変数の中身を返す関数を作る。
関数の宣言の上に@propertyと記述する。
！！注意！！
通常、関数を呼び出す時は関数名の後ろに（）を付けるが、プロパティの場合は（）は付けない。

クラス変数の中身の変更を許可するSetterプロパティ
＠Getterで定義したメソッド名.setter と記述し、その下にSetterメソッドを記述する。
その際に引数はselfの後に変更する値を受け取る変数名を付けてメソッド内で受け取った値をクラス内変数に代入して値を更新する。

これらプロパティを使うのは何か特定の条件の時だけ値を書き換えたいなど。

抽象クラスについて（抽象クラスはそこまで積極的に取り入れる必要はない）
継承先のクラスで必ず必要な関数を入れるには
import abc
とし、親クラスのobjectを(metaclass=abc.ABCMeta)とします。
これによりこのクラスは抽象クラスと認識させる。
継承先クラスで必ず実装させたい関数を記述し、その関数の上に　@abc.abstractmethod　を記述する。
@abc.abstractmethod　を記述する事でクラスを継承したクラスで@abc.abstractmethod以下の関数を記述しないとエラーになる。


"""
import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    # 以下の関数はこのクラスを継承するクラスでは必ず記述しなければならない。
    @abc.abstractmethod
    def drive(self):
        pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No Drive')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('ok')

class Car(object):

    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('Run')

    def ride(self, person):
        person.drive()



class ToyotaCar(Car):

    def run(self):
        print('Fast')


class TeslaCar(Car):

    def __init__(self, model='Model S', enable_auto_run=False, password='123'):
        # self.model = model
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run
        self.password = password

    # プロパティ(Getter)
    @property
    def enable_auto_run(self):
        return self.__enable_auto_run

    # プロパティ(Setter)
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        # パスワードが一致した時のみ、値を書き換える事ができる。
        if self.password == '123':
            self.__enable_auto_run = is_enable
        else:
            raise ValueError

    # 関数
    def run(self):
        print('super fast')

    def auto_run(self):
        print('AutoRun')




# クラスのインスタンスを作成
# Carクラスのインスタンス
car = Car()

# tToyotaCarクラスのインスタンス
toyota_car = ToyotaCar('Lexus')

# TeslaCarクラスのインスタンス
tesla_car = TeslaCar('Model s', password='123')

# Babyクラスのインスタンス
baby = Baby()

# Adultクラスのインスタンス
adult = Adult()




# クラスメソッドの実行
car.run()
car.ride(adult)

# ToyotaCarクラスのインスタンスでCarクラスのメソッドを実行
toyota_car.run()
print(toyota_car.model)

# TeslaCarクラスのインスタンスでCarクラスのrunメソッドを実行
tesla_car.run()
print(tesla_car.model)

# TeslaCarクラスのインスタンスでTeslaCarクラスが持つauto_runメソッドを実行
tesla_car.auto_run()
# tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)