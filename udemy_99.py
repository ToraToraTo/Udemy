
# tarfileの圧縮展開について

from importlib.resources import path
import tarfile

"""
tarfile.open('保存するファイル名', 'w:gz')で圧縮ディレクトリを開く。
その中に.add('圧縮したいディレクトリ名')でディレクトリを圧縮する。
"""
with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

"""
圧縮ディレクトリを展開する。
"""

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    # 全てのファイルを展開する。
    # tr.extractall(path='test_tar')

    # ファイルを展開せずにファイルの中身を確認する。
    with tr.extractfile('test_dir/sub_dir/sub_test.txt') as f:
        print(f.read())