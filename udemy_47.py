
# 辞書をfor文で処理する

d = {'x': 100, 'y': 200}

# items()メソッドを使用する事で第１引数にキーが代入され、第２引数に値が代入される。
for k, v in d.items():
    print(k, ':', v)