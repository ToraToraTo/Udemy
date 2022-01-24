# datetimeについて

import datetime

# 現在時刻を表示する
now = datetime.datetime.now()
print(now)

# 国際規格のISO表記で表示する
print(now.isoformat())

# 任意の表示方法にする
print(now.strftime('%Y/%m/%d - %H:%M:%S'))

# 年を省略して取得
print(now.strftime('%y'))

# 年を全て取得する
print(now.strftime('%Y'))

# 月を取得する
print(now.strftime('%m'))

# 日を取得する
print(now.strftime('%d'))

# 何時を取得する
print(now.strftime('%H'))

# 何分を取得する
print(now.strftime('%M'))

# 何秒を取得する
print(now.strftime('%S'))


# 年月日だけを取得する。
today = datetime.date.today()
print(today)
print(today.strftime('%Y'))
print(today.strftime('%m'))
print(today.strftime('%d'))

# 過去の日付を扱う
# 以下では１週間前の日付を取得している。
d = datetime.timedelta(weeks=1)
print(now)
print(now - d)
print(d)

# 処理の時間を制御する
import time

print('########')
# 処理を1秒止める
time.sleep(1)
print('########')


# バックアップファイルをとる例

import os
import shutil

file_name = 'test.txt'

# 変数file_nameのファイルが存在している場合は現在時刻をつけてバックアップファイルを作成する
if os.path.exists(file_name):
    shutil.copy(file_name, '{}.{}'.format(file_name, now.strftime('%Y_%m_%d_%H_%M_%S')))


# 変数file_nameのファイルが存在していない場合は変数file_nameの名前でファイルを作成し、中身に[Test]と書き込む
with open(file_name, 'w') as f:
    f.write('Test')