
# enumerate関数について

i = 0
for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)
    i += 1

# 同じようにインデックス番号をつけてリストの中身を取り出す時にenumerate関数を用いる。
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)