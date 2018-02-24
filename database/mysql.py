"""
Python3 で MySQL を操作

Python3 には MySQL の標準モジュールはないので、ドライバーをインストール
$ pip install mysqlqlient

PyPI
https://pypi.python.org/pypi/mysqlclient

Github
https://github.com/PyMySQL/mysqlclient-python

Documentation
https://mysqlclient.readthedocs.io/
"""

import MySQLdb

# MySQLの接続情報（各自の環境にあわせて設定のこと）
db_config = {
    'host': 'localhost',
    'db': 'sample_db',  # Database Name
    'user': 'testuser',
    'passwd': 'testpass',
    'charset': 'utf8',
}
# このスクリプトで扱うテーブル名
db_table = 'students'

# データベースに接続
conn = None
try:
    conn = MySQLdb.connect(host=db_config['host'], db=db_config['db'], user=db_config['user'],
                           passwd=db_config['passwd'], charset=db_config['charset'])
    cursor = conn.cursor()
    print('Connection successful.')

    # テーブルの作成
    cursor.execute('DROP TABLE IF EXISTS `students`')
    cursor.execute('''CREATE TABLE IF NOT EXISTS `students` (
        `id` int(11) NOT NULL,
        `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
        PRIMARY KEY (id)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci''')
    print('Create Table successful.')

    ###################
    # INSERT (Create) #
    ###################

    # サンプルデータの追加
    cursor.execute("INSERT INTO students VALUES (1, 'SMITH')")

    # プレースホルダの使用例
    # 1つの場合には最後に , がないとエラー。('JOHNSON') ではなく ('JOHNSON',)
    cursor.execute("INSERT INTO students VALUES (2, %s)", ('JOHNSON',))
    cursor.execute("INSERT INTO students VALUES (%s, %s)", (3, 'WILLIAMS'))
    cursor.execute("INSERT INTO students VALUES (%(id)s, %(name)s)", {'id': 4, 'name': 'JONES'})

    # 複数レコードを一度に挿入 executemany メソッドを使用
    persons = [
        (5, 'BROWN'),
        (6, 'DAVIS'),
    ]
    cursor.executemany("INSERT INTO students VALUES (%s, %s)", persons)

    # コミット（データ保存を実行）
    # commit() を忘れてると保存されないことに注意
    conn.commit()

    ###################
    # SELECT (Read) #
    ###################

    cursor.execute('SELECT * FROM students ORDER BY id ASC')

    # 件数の取得は Cusor オブジェクトの rowcount プロパティー
    print('\ncount')
    print(cursor.rowcount)  # 6

    # 全件取得は cursor.fetchall()
    print('\nfetchall')
    print(cursor.fetchall())
    # ((1, 'SMITH'), (2, 'JOHNSON'), (3, 'WILLIAMS'), (4, 'JONES'), (5, 'BROWN'), (6, 'DAVIS'))

    # 1件取得 cursor.fetchone()
    # fetchone() メソッド実行のたびにカーソル位置が移動します
    print('\nfetchone')
    cursor.execute('SELECT * FROM students ORDER BY id')
    print(cursor.fetchone())  # (1, 'SMITH')
    print(cursor.fetchone())  # (2, 'JOHNSON')
    print(cursor.fetchone())  # (3, 'WILLIAMS')

    # WHERE 句の例
    print('\nWHERE')
    cursor.execute('SELECT * FROM students WHERE name=%s', ('SMITH',))
    print(cursor.rowcount)  # 1
    print(cursor.fetchone())  # (1, 'SMITH')

    # WHERE 句で該当なしの場合
    print('\nNo Result Example')
    cursor.execute('SELECT * FROM students WHERE name=%s', ('TAYLOR',))
    print(cursor.rowcount)  # 0
    print(cursor.fetchall())  # ()
    print(cursor.fetchone())  # None

    # 全件ループ表示方法は2パターン。いずれも同じ結果が得られます。
    print('\nLoop (1)')
    cursor.execute('SELECT * FROM students ORDER BY id ASC')
    for row in cursor:
        print(row)
        '''
        (1, 'SMITH')
        (2, 'JOHNSON')
        (3, 'WILLIAMS')
        (4, 'JONES')
        (5, 'BROWN')
        (6, 'DAVIS')
        '''

    print('\nLoop (2)')
    cursor.execute('SELECT * FROM students ORDER BY id ASC')
    for row in cursor.fetchall():
        print(row)
        '''
        (1, 'SMITH')
        (2, 'JOHNSON')
        (3, 'WILLIAMS')
        (4, 'JONES')
        (5, 'BROWN')
        (6, 'DAVIS')
        '''

    # Tip - MySQLdb.cursors.DictCursor
    print('\nget rows as tuple (default)')
    cursor.execute('SELECT * FROM students ORDER BY id ASC LIMIT 3')
    for row in cursor:
        print(row[0], row[1])
        '''
        1 SMITH
        2 JOHNSON
        3 WILLIAMS
        '''

    print('\nget rows as dictionary')
    dict_cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    dict_cursor.execute('SELECT * FROM students ORDER BY id ASC LIMIT 3')
    for row in dict_cursor:
        print(row['id'], row['name'])
        '''
        1 SMITH
        2 JOHNSON
        3 WILLIAMS
        '''

    ##########
    # UPDATE #
    ##########
    cursor.execute('UPDATE students SET name=%s WHERE id=1', ('MILLER',))
    cursor.execute('UPDATE students SET name=%s WHERE id=%s', ('WILSON', 2))
    conn.commit()

    ##########
    # DELETE #
    ##########
    cursor.execute('DELETE FROM students WHERE id > 3')
    conn.commit()
except MySQLdb.Error as ex:
    print('MySQL Error: ', ex)

if conn:
    conn.close()
    print('\nConnection closed.')
