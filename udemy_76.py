
# importする際の記述の仕方

# ライブラリーをインポートする際に以下のように , で区切ってインポートする事が可能だが、推奨されていない。
import collections, os, sys

# ライブラリーは一つずつインポートしてかつ、アルファベット順でインポート文を記述する。
# また、標準ライブラリーとサードパーティーのライブラリーの間は１行空けてインポートする。
# 自身で作成したパッケージをインポートする際もサードパーティーライブラリーとの間に１行空けてインポートする。
# 最後に１行空けてローカルPythonファイルをインポートする。
# それぞれのインポート文のブロックでアルファベット順に揃えて記述する。

import collections
import os
import sys

import termcolor

import lesson_package

import config


# ファイルの確認
print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print(sys.path)