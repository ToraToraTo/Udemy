
# キーワード引数の辞書化について

def menu(entree='beef', drink='wine'):
    print(entree, drink)

menu(entree='beef', drink='coffee')



# 引数に **kwargs を指定する事で、引数を辞書型で受け取る事ができる。
# 以下では受け取った辞書型引数をループでキーと値を取り出して表示している。
def menu_dig(**kwargs):

    for k, v in kwargs.items():
        print(k, v)

menu_dig(entree="beef", drink='coffee')




# 引数に渡す辞書を予め用意してそのまま引数に渡すには先頭に ** をつけて渡す。
d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}

menu_dig(**d)



# 複数の引数を*argsや**kwargsで指定して渡す
def menu_function(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu_function('banana', 'apple', 'orange', entree='beef', drink='coffee')