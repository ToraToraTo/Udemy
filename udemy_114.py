
# 変数に値を代入する際にif文を使う
# 以下の条件の場合、もしyに何か入っていれば１を代入し、そうでなければ２を代入する。

y = None
x = 1 if y else 2

print(x)

# リストの初期化について
# デフォルト引数の時にそこでリストを初期化すると問題が起きるので以下のようにする。

def sum(a, lists=None):

    # リストの初期化
    if lists is None:
        lists = []


