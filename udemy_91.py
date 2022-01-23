
# ファイルの作成
"""
ファイルに書き込む時は基本的にwrite()を使う。

open()のオプションではaを指定すると追加で書き込み、wを指定すると上書きする。
asの後ろは変数名を指定する。
withステートメントを使う事でopenで開いたファイルを中の処理が終了した時に自動的に閉じる処理を行う。
withステートメントは他の場合でも何かの処理を行った後に自動的に終了するなど、使う場面が多い。
"""

s = """\
AAA
BBB
CCC
DDD
"""

# ファイルを開く
# with open('test.txt', 'w') as f:
#     # ファイルに書き込む
#     f.write(s)
    # print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)

#ファイルの読み込み

with open('test.txt', 'r') as f:

    # １行ずつ読み込む
    # while True:
        # 何行事に読み込むかを指定するchunk
        # chunk = 2
        # readline()で１行ずつの読み込みを行う。
        # line = f.readline()
        # line = f.read(chunk)
        # print()では自動的に改行を行うので、end=''で改行を行わないようにする。
        # print(line, end='')
        # print(line)
        # lineに何も入ってなかったらbreakで処理を終了する。
        # if not line:
        #     break

    # .tell()で何行目かを出力
    print(f.tell())

    # .read(1)で今セットされてる行の１文字だけを取り出す
    print(f.read(1))

    # .seek()で任意の位置に移動
    f.seek(5)
    print(f.read(1))
    f.seek(14)
    print(f.read(1))
