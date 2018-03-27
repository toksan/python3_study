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
