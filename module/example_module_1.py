"""
モジュールの利用
同一階層の他ファイルで定義されている関数やクラスを利用するサンプル
"""

# 同一階層にある hoge.py を利用するためインポート（拡張子 .py は不要）
import hoge

# hoge.py で定義されている変数を使用
print(hoge.hoge_var)  # 'Dog and Cat'

# hoge.py で定義されているsquare()関数を使用
print(hoge.square(7))  # 49

# hoge.py で定義されているCalculatorクラスを利用
calc = hoge.Calculator()

# インスタンスメソッドを実行
print(calc.get_version())  # '1.0.1'

# スタティックメソッドを実行
print(hoge.Calculator.cube(2))  # 8
