"""
ラムダのサンプル
"""

# 名前:年齢　の辞書型データ（dict）
dict_staff = {
    'suzuki': 51,
    'tanaka': 25,
    'yamada': 40,
    'kimura': 33,
}

# 年齢昇順に並び替え
sorted_staff = sorted(dict_staff.items(), key=lambda x: x[1])
for name, age in sorted_staff:
    print(name, age)

# 年齢降順に並び替え
print('--- Reverse ---')
sorted_staff = sorted(dict_staff.items(), key=lambda x: x[1], reverse=True)  # reverse=True
for name, age in sorted_staff:
    print(name, age)

print('--- キー:バリューが逆の場合（キーを基準に並び替え） ---')
dict_staff = {
    51: 'suzuki',
    25: 'tanaka',
    40: 'yamada',
    33: 'kimura',
}

# 値を基準に並び替える場合は x[1] だったが、キーを規準にする場合は x[0] にする
sorted_staff = sorted(dict_staff.items(), key=lambda x: x[0])
for age, name in sorted_staff:
    print(name, age)

print('--- キーで並び替える場合にはlambdaは省略OK ---')
# sorted()はkeyを明示的に指定しない場合（デフォルトの場合）キーを基準に並び替えるので lambad は不要
sorted_staff = sorted(dict_staff.items())
for age, name in sorted_staff:
    print(name, age)

print('--- タプルのリストをソートするサンプル（公式ドキュメント） ---')
# @see: http://docs.python.jp/3.3/howto/sorting.html
student_tuples = [
    ('john', 'A', 15),  # name, grade ,age
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted_student_tuples = sorted(student_tuples, key=lambda student: student[2])  # sort by age
print(sorted_student_tuples)
