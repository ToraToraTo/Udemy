
# 例外処理について

l = [1, 2, 3]
i = 5
# del l

"""
tryとexceptの間にエラーが起きそうな処理を記述する事で、もしエラーになってもプログラムを終了させずに処理を続行する事ができる。
exceptの下にエラーが発生した時の処理を記述する。
また、exceptの後ろにIndexError as ex と記述すると、変数exにインデックスエラーの内容が格納されるので、エラー内容を表示させる事もできる。
複数のエラーパターンの為、exceptを追加で記述して複数に対応する事も可能。
全てのエラー内容を表示するにはExceptionを使う。

finallyを最後に記述するとexceptionがあったとしても最後に必ずfinallyが実行される。
else を記述すると、exceptionが何も発生しない時だけ実行される。
つまり、tryが成功した後にelseに記述した処理を実行して、最後にfinallyに記述した処理を実行する。
"""
try:
    l[0]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print(ex)
else:
    print("done")
finally:
    print("clean up")