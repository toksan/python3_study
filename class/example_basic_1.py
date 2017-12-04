"""
Python のクラスとオブジェクト学習用 基本サンプル
"""


class Item:
    """
    商品クラス
    """

    """
    商品リスト
    Pythonではメソッド外で定義した変数は「クラス変数」になる点に注意しましょう。
    クラス変数はこのクラスから生成したすべてのインスタンスで共有されます。
    商品リストをクラス変数にする必要はありませんが、サンプルのためクラス変数にしてみました。
    """
    item_list = [
        {'name': 'None', 'price': 0},
        {'name': 'pencil', 'price': 100},
        {'name': 'eraser', 'price': 80},
        {'name': 'compass', 'price': 300},
    ]

    def __init__(self, item_id):
        """
        コンストラクタ
        :param item_id: 商品ID
        """
        item = self.search_item_by_id(item_id)
        # メソッド内で self.name のように定義すると「インスタンス変数」になります。
        # インスタンス変数は生成したインスタンス固有のものとなります。
        self.id = item_id
        self.name = item['name']
        self.price = item['price']

    def search_item_by_id(self, item_id):
        """
        商品情報をセット
        :param item_id: 商品ID
        :rtype: dict
        :return: 商品データ（辞書型）
        """
        # 簡単のためitem_idのチェックは省略
        return self.item_list[item_id]


class Cart:
    """
    ショッピングカートクラス
    """

    def __init__(self):
        self.items = []

    def add_item(self, item, number):
        """
        商品をカートに加える
        :param item: Itemオブジェクト
        :param number: 数量
        :return: None
        """
        for i in range(number):
            # 説明のため print() しますが、ビュー以外で print() するのは保守性を著しく低下させるのでやめましょう。
            print(item.name + ': ' + str(item.price) + '円')
            self.items.append(item)

    def calc_subtotal(self):
        """
        小計を計算
        :return: 小計金額
        """
        p = 0
        for item in self.items:
            p += item.price
        return p

    @staticmethod
    def add_tax(price):
        """
        税を加算（税込金額を取得）
        メソッド定義の直前に @staticmethod デコレータを書くとスタティックメソッドになります。
        スタティックメソッドはインスタンス化なしに使用できる静的メソッドです。
        引数に self は不要となる点に注意しましょう。

        :param price: 金額
        :return: 税込価格
        """
        return int(round(price + price * TAX_RATE * 0.01))


# 税率を設定
TAX_RATE = 8

# 商品をカートに追加して小計と合計を計算
my_cart = Cart()
my_cart.add_item(Item(1), 2)  # 鉛筆2個
my_cart.add_item(Item(2), 1)  # 消ゴム1個
my_cart.add_item(Item(3), 1)  # コンパス1個
subtotal = my_cart.calc_subtotal()  # 小計
# staticmethod はインスタンス化せず クラス名.メソッド名() で実行可能。
total = Cart.add_tax(subtotal)  # 合計

print('----------------')
print('小計: ' + str(subtotal) + '円')
print('合計: ' + str(total) + '円')
print('----------------')

# staticmethod は インスタンス.メソッド名() でも実行可能です。
print('合計: ' + str(my_cart.add_tax(subtotal)) + '円 - インスタンスメソッドで計算')
