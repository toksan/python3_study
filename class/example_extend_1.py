"""
Python のクラスとオブジェクト学習用 継承のサンプル
"""


class BookStore:
    def __init__(self, id):
        """
        コンストラクタ
        :param id: 店舗ID
        """
        self.id = id

    def has_branch(self):
        """
        支店を持っているか
        :return:
        """
        return True

    def search_book(self, book_name):
        """
        店舗に書籍があるかを検索
        :param book_name: 書籍名
        :return:
        """
        # 実際にはDB処理等を行うがここでは省略
        # 下の本が見つかったとする
        book = {'id': 123, 'name': 'はじめてのPython（仮）', 'price': 3000}
        return book


class TokyoBookStore(BookStore):
    def __init__(self, id):
        super().__init__(id)
        self.name = 'ABC書房 東京店'

    def has_branch(self):
        """
        オーバーライド（基底クラスと同じ名前のメソッドを定義して処理内容を上書き）
        :return:
        """
        return False

    def search_stationery(self, item_name):
        """
        東京店では文房具の取り扱いもあるのでメソッドを追加
        :param item_name: 商品名
        :return:
        """
        # 実際にはDB処理等を行うがここでは省略
        # 下の文房具が見つかったとする
        item = {'id': 777, 'name': 'ボールペンA', 'price': 100}
        return item


tokyo_store = TokyoBookStore(13)
print(tokyo_store.id)
print(tokyo_store.name)
print(tokyo_store.has_branch())
print(tokyo_store.search_book('Python'))
print(tokyo_store.search_stationery('ペン'))
