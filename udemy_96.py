
# テンプレートについて

"""
テンプレートの作成をするには import string を行う。
テンプレートの中身で後から文字列を代入したい場所に$を先頭に付ける。
$の後ろには変数名を付ける。

テンプレートを代入する変数を定義し、string.Template(文字列の変数名) を代入する。
テンプレートが代入された変数に、.substitute(＄を付けた変数名＝'代入文字列')としてテンプレートに文字列を代入する。

テンプレートを使う事で元の文字列が壊される危険がなくなる。
ただし、テンプレートが代入されている変数に直接何かを代入されるとテンプレートの中身が壊れるので必ずTemplateで行う必要がある。
"""


import string

s = """\

Hi $name.

$contents

Have a good day

"""

# withで別のディレクトリーからテンプレートファイルを読み込んで、Template処理を行う。
# withの中で宣言した変数はwithの外でも使える。
with open('design/email_template.txt') as f:
    t = string.Template(f.read())


contents = t.substitute(name='Mike', contents='How are you?')
print(contents)