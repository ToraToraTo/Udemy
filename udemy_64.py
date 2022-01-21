
# 名前空間とスコープについて

animal = 'cat'

# Function内からグローバル変数を使う
def f():
    print(animal)

f()

def f_2():
    animal = 'dog'
    print('after:', animal)

f_2()
print('global:', animal)


# 関数の中でグローバル変数にアクセスするには先頭に　global　と付けて変数名を記述する。

def f_global():
    global animal
    animal = 'dog'
    print('local:', animal)

f_global()
print('global:', animal)