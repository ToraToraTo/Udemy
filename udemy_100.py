# zipファイルの圧縮と展開について

import zipfile
import glob

"""
with zipfile.ZipFile('作成するzipファイルの名前', 'w') as z:
    z.write('zipファイルの中に作成するディレクトリ名')
    z.write('作成したディレクトリ名/ディレクトリの中に作成するファイル名と拡張子')
"""
with zipfile.ZipFile('test.zip', 'w') as z:
    z.write('test_dir')
    z.write('test_dir/test.txt')


# 読み込み
with zipfile.ZipFile('test.zip', 'r') as z:
    # z.extractall('zzz2')
    with z.open('test_dir/test.txt') as f:
        print(f.read())