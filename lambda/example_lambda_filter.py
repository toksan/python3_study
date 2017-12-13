"""
ラムダのサンプル
"""

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = filter(lambda x: x % 2 == 0, list_1)  # 偶数のみにフィルター

# Python3でfilter()関数の仕様が変りました
# Python2系では [2, 4, 6, 8] というリストが返ってきていましたが、3系では filter object が返ってきます
print(list_2)  # <filter object at XXXXXXXX>

# Python3でリストとして取得するしたい場合
list_2 = list(filter(lambda x: x % 2 == 0, list_1))
print(list_2)  # [2, 4, 6, 8]

# tuple()関数を使うとタプルとして取得も可能
list_3 = tuple(filter(lambda x: x % 2 == 0, list_1))
print(list_3)  # (2, 4, 6, 8)

# 文字列でフィルターするサンプル
list_s_1 = ['apple', 'grape', 'banana', 'orange']
list_s_2 = list(filter(lambda x: 'n' in x, list_s_1))  # 'n' を含むかでフィルター
print(list_s_2)  # ['banana', 'orange']
