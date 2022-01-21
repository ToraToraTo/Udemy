
# ジェネレーターについて
"""
ジェネレーターは関数で定義するが、戻り値はない。
関数内にyieldを記述する事で自動的にジェネレーターとして認識する。
ジェネレーターを使う事で処理の途中で別の処理を実行する事ができる。
重たい処理をいっきに実行するのではなく、ジェネレーターを用いて小分けにして実行する時にもジェネレーターが使える。

"""

l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print("###########################################")

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

for i in greeting():
    print(i)

print("#############################################")

# ジェネレーターを使う事で順番に取り出しながら任意の場所で他の処理を実行する事ができる。
g = greeting()

print(next(g))
print('@@@')
print(next(g))
print('@@@')
print(next(g))
print('@@@')


# 例２
print('####################################################')

def counter(num=10):
    for _ in range(num):
        yield 'run'


c = counter()
gc = greeting()

print(next(gc))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(gc))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(gc))