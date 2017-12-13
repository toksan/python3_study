"""
モジュールの利用
同一階層の他ファイルで定義されている関数やクラスを利用するサンプル
"""

# 同一階層にある hoge.py を利用するためインポート（拡張子 .py は不要）
# from モジュール名 import 要素名
from hoge import hoge_var, square, Calculator

# *（アスタリスク）を使うとモジュール内の要素をまとめてインポートできる（ただし非推奨）
# @see: https://docs.python.jp/3/tutorial/modules.html
# from hoge import *


# import モジュール名　だと呼び出し時に hoge.square() のように書く必要があったが
# from モジュール名 import 要素　の場合には hoge. が不要で square() と簡潔に書ける

# hoge.py で定義されている変数を使用
print(hoge_var)  # 'Dog and Cat'

# hoge.py で定義されているsquare()関数を使用
print(square(7))  # 49

# hoge.py で定義されているCalculatorクラスを利用
calc = Calculator()

# インスタンスメソッドを実行
print(calc.get_version())  # '1.0.1'

# スタティックメソッドを実行
print(Calculator.cube(2))  # 8
