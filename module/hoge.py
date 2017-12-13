"""
hogeモジュール

１ファイルにあれこれ定義するのはよくないですが、
サンプル簡潔化のため関数とクラスをごちゃ混ぜで定義
"""

hoge_var = 'Dog and Cat'

def square(x):
    return x ** 2


class Calculator:
    def __init__(self):
        self.version = '1.01'

    def get_version(self):
        return self.version

    @staticmethod
    def cube(x):
        return x ** 3
