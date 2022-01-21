
# サードパーティーライブラリーについて
# https://pypi.org/

from termcolor import colored

print('test')

# Textの色を変更して出力する。
print(colored('test', color='yellow'))

# help関数でcoloredの使い方を確認できる。
print(help(colored))