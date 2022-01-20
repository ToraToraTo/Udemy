
# ラムダについて
"""
リストlには一部がキャピタルになっていないものが入ってます。
change_words関数では引数でキーワードと関数を受け取り、キーワードのリストの中身を一つずつ取り出し、キャピタルに変換する関数に値を渡します。
change_words関数の第二引数のfuncにはsample_func関数が代入されており、ループ内でキーワードをsample_func関数に代入しています。
sample_func関数内のcapitalize()は文字列をキャピタルに変換します。
"""
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))


# def sample_func(word):
#     return word.capitalize()

# 上記の関数を簡略化して記述すると以下のようにlambdaを用いて記述する事が出来る。
"""
ラムダの記述方法
関数名に＝をつけ、lambdaと記述する。
lambdaの後に引数名と：をつけて、最後に戻り値の処理を記述する。
また、変数に代入せずに関数を引数とする関数の引数に直接ラムダで記述する事でコードを簡略化する事ができる。
"""
sample_func = lambda word: word.capitalize()

change_words(l, sample_func)

# ラムダを直接関数の引数に記述した例。　.lower()で全て小文字にする事ができる。
change_words(l, lambda word: word.lower())
