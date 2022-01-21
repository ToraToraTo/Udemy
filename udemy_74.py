
# 標準ライブラリーについて
# Pythonの標準ライブラリについて詳細は以下のURL
# https://docs.python.org/ja/3/library/

# Collections --コンテナデータ型について
# 以下の文字列の中で特定のアルファベットが何個あるか？を調べる
s = "adsahfeoj.heisiafbejkanfdj"

d = {}

for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1

print(d)

# setdefault（）を使う事でもしキーcの値が何もない場合は０を入れる。
# そうでないなら、キーcの値を＋１する。
d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1

print(d)

# 標準ライブラリーを使う場合は必ずインポートしないと使えない。
from collections import defaultdict

# 以下で０が入る。
d = defaultdict(int)

for c in s:
    d[c] += 1

print(d)
print(d['a'])