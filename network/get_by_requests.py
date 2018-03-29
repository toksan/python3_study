"""
Requests モジュールによりリモートファイルを読み込むサンプル

事前にRequestsモジュールをインストールしましょう
# pip install requests
"""
import requests

url = 'https://it-engineer-lab.com/feed'
try:
    r = requests.get(url, timeout=10.0)
    print(r.text)
except requests.exceptions.RequestException as err:
    print(err)


# ダウンロード（読み込み + ローカル保存）
# ダウンロードして rss.xml というファイル名で保存する例
try:
    r = requests.get(url, timeout=10.0)
    with open('rss.xml', mode='w') as f:
        f.write(r.text)
except requests.exceptions.RequestException as err:
    print(err)