"""
ラムダのサンプル
"""

list_1 = [1, 3, 5]
list_2 = map(lambda x: x * 2, list_1)

# Python3でmap()関数の仕様が変りました
# Python2系では [2, 6, 10] というリストが返ってきてい　ましたが、3系では map object が返ってきます
print(list_2)  # <map object at XXXXXXXXX>

# Python3でリストとして取得するしたい場合
list_2 = list(map(lambda x: x * 2, list_1))
print(list_2)  # [2, 6, 10]

# tuple()関数を使うとタプルとして取得も可能
list_3 = tuple(map(lambda x: x * 2, list_1))
print(list_3)  # (2, 6, 10)

# 文字列連結の例
list_s_1 = ['高橋', '鈴木', '渡辺']
list_s_2 = list(map(lambda x: x + '様', list_s_1))
print(list_s_2)  # ['高橋様', '鈴木様', '渡辺様']
