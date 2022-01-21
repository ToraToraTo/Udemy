
# 別のディレクトリーにあるモジュールを読み込む
from lesson_package.tools import utils

def sing():
    return 'fhjiewofgerpwsing'

def cry():
    return utils.say_twice('feksagjriopcry')

if __name__ == '__main__':
    print(sing())
    print('animal:', __name__)
