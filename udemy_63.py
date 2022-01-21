
# ジェネレーター内包表記について

def g():
    for i in range(10):
        yield i

g = g()

print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# 上記のジェネレーターを内包表記で記述する。
"""
ジェネレーターを内包表記で記述する時、（）でかこって記述するのでタプルになりそうですが、（）に何もつけずに以下の記述にするとジェネレーターになる。
もし、タプルにしたい場合は（）の前に　tuple　を付ける必要があるので注意が必要！
"""
print("#########################################")
g = (i for i in range(10))
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print("##########################################")
# 条件を付けたジェネレーター
g = (i for i in range(10) if i % 2 == 0)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# Tupleでの内包表記では（）の前にtupleを付ける。
gt = tuple(i for i in range(10))
print(type(gt))
print(gt)