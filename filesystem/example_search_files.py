"""
特定のディレクトリ下のファイル一覧を取得するサンプル

公式ドキュメント
https://docs.python.jp/3/library/os.html
https://docs.python.jp/3/library/os.path.html
"""

import os

"""
様々なディレクトリについてファイル一覧を取得
末尾のスラッシュ（ディテクトリセパレータ・ファイル区切り文字）はあってもなくてもOK
"""
# カレントディレクトリのファイル一覧
print(os.listdir('.'))
print(os.listdir('./'))

# カレントディレクトリより一階層上のディレクトリのファイル一覧
print(os.listdir('..'))
print(os.listdir('../'))

# /var/log ディレクトリのファイル一覧
print(os.listdir('/var/log'))
print(os.listdir('/var/log/'))

# 存在しないディテクトリだとエラーになるので存在しない可能性があるディテクトリは os.path.isdir() で存在確認
# print(os.listdir('/var/notfonud_dir'))
target_dir = '/var/not_exist_dir'
if os.path.isdir(target_dir):
    print(os.listdir(target_dir))
else:
    print('Error:' + target_dir + ' does not exist.')

# os.listdir() はファイルとディテクトリの区別なく一緒くたに取得される
# ファイルとディテクトリを区別して表示するサンプル
target_dir = '/var/log'
for i in os.listdir(target_dir):
    abs_path = target_dir + '/' + i  # target_dir + os.sep + i;
    if os.path.isfile(abs_path):
        print('File: ' + i)
    elif os.path.isdir(abs_path):
        print('Directory:' + i)
