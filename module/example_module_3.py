"""
モジュールの利用
異なる階層にある他ファイルで定義されている関数やクラスを利用するサンプル
子ディテクトリ（一階層下）の場合
"""

# ディテクトリの区切り文字に . を用いる（ / ではない）
# import sub_dir/hogehoge  はシンタックスエラー
import sub_dir.hogehoge

sub_dir.hogehoge.say_hello()
