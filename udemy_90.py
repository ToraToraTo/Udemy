
# 特殊メソッドについて


class Word(object):

    def __init__(self, text):
        self.text = text

    # 文字列を受け取った時に呼ばれるメソッド(よく使う)
    def __str__(self):
        return "Word!!!!!!!!!"

    # len関数を使ったら呼ばれるメソッド
    def __len__(self):
        return len(self.text)

#     クラス内のデータの足し合わせ
    def __add__(self, word):
        return self.text.lower() + word.text.lower()

#     クラス内のデータが等しいかどうかを判定
    def __eq__(self, word):
        return self.text.lower() == word.text.lower()



w = Word('test')
w2 = Word('#####')

print(w)

print(len(w))

print(w + w2)

print(w == w2)