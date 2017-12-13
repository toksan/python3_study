"""
モジュールの利用
異なる階層にある他ファイルで定義されている関数やクラスを利用するサンプル
親ディテクトリ（一階層上）の場合
"""

# 標準モジュール sys をまずインポート
import sys

# 階層が上のディレクトリで定義された要素をインポートするのはひと手間が掛かる
# モジュール検索パスに親ディレクトリを追加
# サンプルのためここでは相対パスで指定するが通常は絶対パスで指定する
sys.path.append('..')  # sys.path.append('../') でもOK

import hoge

# ../hoge.py で定義されている変数を使用
print(hoge.hoge_var)  # 'Dog and Cat'

# ../hoge.py で定義されているsquare()関数を使用
print(hoge.square(7))  # 49
