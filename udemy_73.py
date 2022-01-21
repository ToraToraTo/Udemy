
# 組み込み関数について
# 組み込み関数について詳しくは以下のURLから参照
# https://docs.python.org/ja/3/library/functions.html


print(globals())


ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

# sorted()を使う事で並び替えを行う。
print(sorted(ranking))

print(ranking.get('A'))

# key=にgetを付ける事でキーに対応した値で並び替えを行う。
print(sorted(ranking, key=ranking.get))

# 並び順を反転するにはreverse＝True とする事で並び順を反転する。
print(sorted(ranking, key=ranking.get, reverse=True))