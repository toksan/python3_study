"""
urllib モジュールによりリモートファイルを読み込むサンプル
"""
import urllib.request
from urllib.error import URLError

url = 'https://it-engineer-lab.com/feed'
try:
    with urllib.request.urlopen(url) as f:
        print(f.read().decode('utf-8'))  # print(f.read())  <- binary
except URLError as e:
    # https://docs.python.jp/3/howto/urllib2.html#wrapping-it-up
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
