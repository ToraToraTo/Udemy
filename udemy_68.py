
# import文とasについて

"""
モジュールを自身で作成する
作業ディレクトリーに新たにモジュール用のディレクトリを作成する。
モジュール用ディレクトリー内にモジュールを記述するファイルと、__init__というファイル名のPythonFileを作成する。
__init__ファイルがないと、モジュールファイルを読み込めない状態になるにで必ず作成する。

作成したモジュールを読み込むには最初にパッケージディレクトリー名と記述し、. で繋いでモジュールが記述されているファイル名を記述する。
"""

import lesson_package.tools.utils

from lesson_package.tools import utils, utils as u

# この記述方法だとどこの関数かが後々分かりづらいので使用しない
from lesson_package.tools.utils import say_twice


r = lesson_package.tools.utils.say_twice("Heelo")
print(r)

r2 = utils.say_twice("Hello")
print(r2)

r3 = say_twice("Hello")
print(r3)


# importする際に任意の名前で読み込むには最後に as を付けて読み込む。
# あまり簡略化するとわかりずらくなるので、基本的に使わない方がいい。

r4 = u.say_twice('Hello')
print(r4)

"""
パッケージのディレクトリーの中のディレクトリーの中にあるモジュールファイルを読み込む。

"""
from lesson_package.tolk import human

print(human.sing())

print(human.cry())


print("################################################")
"""
同じディレクトリー内にある全てのモジュールファイルを読み込む
読み込みたいモジュールディレクトリーの__init__ファイルに　__all__ = ['モジュールファイル名']　を記述する。
モジュールを読み込み際に import * とする。
しかし、この方法でモジュールを読み込むと何が読み込まれているのかが不明確の為、あまり使わない。
"""
from lesson_package.tolk import *

print(animal.sing())
print(animal.cry())

print("####################################################")

"""
import Errorについて
新しいパッケージと古いパッケージの両方を使う際に、インポートエラーを回避する目的で以下のように記述する。
"""
try:
    from lesson_package import utils
except:
    from lesson_package.tools import utils

utils.say_twice('word')