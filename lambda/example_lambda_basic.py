"""
ラムダのサンプル
"""

# Basic

# 引数を3倍するラムダ式（無名関数）
x3 = lambda arg: arg * 3

print(x3(1))  # 3
print(x3(5))  # 15

# 奇数かを判定するラムダ式（無名関数）
is_odd = lambda arg: arg % 2 != 0

print(is_odd(4))  # False
print(is_odd(7))  # True

# lambda内でif文を使うサンプル。冗長ながら上記をあえてif/elseで実装。
is_odd_use_if = lambda arg: True if arg % 2 != 0 else False

print(is_odd_use_if(4))  # False
print(is_odd_use_if(7))  # True


# 関数の定義を使うと以下のようになる
def normal_x3(arg):
    return arg * 3


print(normal_x3(1))  # 3
print(normal_x3(5))  # 15
