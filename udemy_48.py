
# 関数の定義について

def say_something():
    print('Hi')

# 関数の呼び出し
say_something()



# 戻り値のある関数の定義
def say_something_return():
    s = 'Hi'
    return  s

# 戻り値を変数に代入
result = say_something_return()

# 戻り値が代入された変数を出力
print(result)



# 引数のある関数の定義
def what_is_thia(color):
    print(color)

# 関数を呼び出す時に引数を渡す
what_is_thia('Red')



# 型を指定して関数を定義する
# 引数の型を指定しても指定型以外の型の値を代入してもエラーにはならないので注意。基本的にこの書き方はしない。
def add_num(a: int, b: int) -> int:
    return a + b

num_result = add_num(1, 3)
print(num_result)



# 位置引数、キーワード引数、デフォルト引数について

def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)

# 複数の引数を扱う時はキーワードアーギュメントを使用して、引数を渡すと間違いが起きない。
menu(entree='beef', drink='beer', dessert='ice')




# デフォルト引数は予め関数に引数を渡した状態で定義している。
def menu_2(entree='beef2', drink='beer2', dessert='ice2'):
    print(entree)
    print(drink)
    print(dessert)

# 引数を何も与えない場合はデフォルト引数がそのまま渡される
menu_2()

# 引数を何か与える事でデフォルト引数の部分が渡した引数に置き換わる
menu_2(entree='chicken', drink='wine')



# デフォルト引数で注意する事！！
def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)



# 以下のようにするとlのアドレスは１度しか生成されていないので、最初の１００が残ったままになる。
# そのため、関数のデフォルト引数にリストや辞書を指定するとバグに繋がるので行わないようにする。
r_2 = test_func(100)
print(r_2)

r_2 = test_func(100)
print(r_2)




# 空のリストを関数で扱いたい場合は、Noneを使う
def test_function(x, l=None):

    # もしlがNoneの時は空のリストでlを初期化する。
    if l is None:
        l = []

    l.append(x)
    return l

r_3 = test_function(100)
print(r_3)

r_3 = test_function(100)
print(r_3)

