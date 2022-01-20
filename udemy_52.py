
# 位置引数のタプル化について

def say_something(word):
    print(word)

say_something('Hi!')



# 複数の引数をタプルでまとめて処理するには *args を使用する
def say_sumething_args(*args):
    for arg in args:
        print(arg)

say_sumething_args('Hi!', 'Maik', 'Nancy')



# 複数の引数で最初の引数だけは必ず入り、残りの引数が何個引数が入るか分からない場合には、最初の引数だけ引数名を指定して、最後に *args を指定する。
def say_something_function(word, *args):
    print('word=', word)
    for arg in args:
        print(arg)

say_something_function('Hi!', 'Maik', 'Nancy')


# 複数の引数を予めタプルにしてそのタプルの変数を引数に渡す場合は先頭に * をつけて渡す。
t = ('Maik', 'Nancy')
say_something_function('Hi!', *t)
