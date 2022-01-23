
# ファイル操作について

import os
import pathlib
import glob
import shutil

"""
# os.path.exists(ファイル名)でこのファイルが存在するかをブールで返す
"""
print(os.path.exists('test.txt'))



"""
# os.path.isfile(ファイル名)でこのファイルはファイルですか？というのをブールで返す
"""
print(os.path.isfile('test.txt'))



"""
# os.path.isdir(ディレクトリ名)でディレクトリかどうかをブールで返す
"""
print(os.path.isdir('design'))



"""
# os.rename(変更したいファイル名, 変更後のファイル名)でファイル名を変更する
"""
# os.rename('test.txt', 'renamed.txt')


"""
# os.symlink(リンク元のファイル名, 生成するファイル名)でSymlinkファイルを生成する。
# Symlinkファイルの中身を書き換えるとリンク元の中身も書き換えられる。
"""
# os.symlink('renamed.txt', 'symlink.txt')


"""
# os.dir(ディレクトリの名前)でディレクトリを作成する
"""
# os.mkdir('test_dir')


"""
# os.rmdir(ディレクトリ名)でディレクトリを削除する
# 削除するディレクトリ内に何も入っていない場合のみ使う事ができる。
"""
# os.rmdir('test_dir')


"""
# ディレクトリ内に他のファイルやディレクトリが存在している場合にまとめて削除する
"""
# shutil.rmtree('test_dir')


"""
# pathlib.Path('ファイル名').touch()で空のファイルを生成する。
"""
# pathlib.Path('empty.txt').touch()


"""
# os.remove(ファイル名)でファイルの削除
"""
# os.remove('empty.txt')


"""
# os.listdir(ディレクトリ名)でそのディレクトリ内になんのディレクトリがあるかを確認
"""
# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# print(os.listdir('test_dir'))



"""
# glob.glob(調べたいディレクトリのパス/*)とすると、指定したディレクトリ内の全てのファイルを表示する。　＊は全てを表示
"""
# print(glob.glob('test_dir/test_dir2/*'))



"""
# shutil.copy(コピー元のファイルパス, コピー先のファイルパス（ファイル名））で指定したファイルをコピーする
"""
# shutil.copy('test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt')
# print(glob.glob('test_dir/test_dir2/*'))


"""
現在の作業ディレクトリを表示するには os.getcwd() で表示
"""
print(os.getcwd())