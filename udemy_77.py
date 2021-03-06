
# __name__ と __main__ について

import lesson_package.tolk.animal

import config

"""
__name__ とすると、今実行しているファイルがメインで動いているのかを返してくれる。
結果が__main__だった時、現在のファイルがメインで動いているという事になる。

他のファイルまたはパッケージをインポートで読み込む際、そこに記述されている文がすぐに実行されるので、呼び出す文を直接記述するのではく、
関数内にパッケージ内の関数を呼び出すコードを記述し、以下の条件分のように__main__の時に関数を呼び出して実行されるようにする。
こうする事で、他の人がこのファイルをインポートした時に勝手に実行される事を防止する事ができる。
"""


def main():
    lesson_package.tolk.animal.sing()

if __name__ == '__main__':
    main()


print('lesson:',__name__)