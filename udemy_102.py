# subprocessコマンドについて

"""
subprocessはターミナル上で行っているコマンドをPython上から行う

import subprocess
を行い、コマンドを実行するには subprocess.run(['コマンド']) で実行する。
"""

import subprocess

subprocess.run(['ls'])
r = subprocess.run(['ls', '-al'])

# returncodeが０でない場合はコマンドに間違いがあり実行されない。その場合でもそのまま次のコードが処理されるので、Exceptionを実行する事で処理を可変できる。
print(r.returncode)
