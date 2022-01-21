
# 辞書包括表記について

w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}

for x, y in zip(w,f):
    d[x] = y

print(d)

print("###################################")
# 上記のループを内包表記で記述する。
# 内包表記の方法としてはリスト内包表記と同じであるが、キーとバリューは　:　で区切り記述する。

d = {x: y for x, y in zip(w, f)}

print(d)