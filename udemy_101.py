# tempfileについて

import tempfile

with tempfile.TemporaryFile(mode='w+') as t:
    t.write('Hello')
    t.seek(0)
    print(t.read())


with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# 一時的なディレクトリの作成
with tempfile.TemporaryDirectory() as td:
    print(td)

# 削除されずに残るディレクトリの作成
temp_dir = tempfile.mkdtemp()
print(temp_dir)

