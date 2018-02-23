"""
SQLAlchemy によるデータベース操作

Website
https://www.sqlalchemy.org/

Document
http://docs.sqlalchemy.org/en/latest/orm/tutorial.html

"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

# 1. データベースエンジンの作成
# SQLite - Memory
engine = create_engine('sqlite:///:memory:')
# engine = create_engine('sqlite:///:memory:', echo=True)  # echo=True if you need SQL log

# SQLite - File
# engine = create_engine('sqlite:///sample_db.sqlite3')

# MySQL
# engine = create_engine('database://testuser:testpass@localhost/sample_db?charset=utf8')

# 2. モデルの作成
# 説明のためファイル内に定義しますが、実際は別ファイル化して import します。
Base = declarative_base()


class Student(Base):
    """
    生徒モデル
    必ず Base を継承
    """
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    score = Column(Integer)  # 点数

    def __repr__(self):
        return "<Student(id='%s', name='%s', score='%s')>" % (self.id, self.name, self.score)


# 3. テーブルの作成
# テーブルがない場合 CREATE TABLE 文が実行される
Base.metadata.create_all(engine)

# 4. セッションの作成
# SQLAlchemy はセッションを介してクエリを実行する
Session = sessionmaker(bind=engine)
session = Session()

###########################
# 以上で準備完了。
# ここからクエリを実行していきます。
############################

# 念のためデータを全削除
session.query(Student).delete()
session.commit()

# SQLを直接実行してもOK
# engine.execute('DELETE FROM students')

###################
# INSERT (Create) #
###################
# 1レコードの追加
session.add(Student(id=1, name='Suzuki', score=70))

# 複数レコードの追加
session.add_all([
    Student(id=5, name='Yamada', score=73),
    Student(id=7, name='Watanabe', score=88),
    Student(id=10, name='Tanaka', score=65),
])

# コミット（データ追加を実行）
session.commit()

#################
# SELECT (Read) #
#################

# Read All
# 全件取得
print('\nSELECT all()')
result = session.query(Student).all()  # .all() は省略可
for student in result:
    print(student.name, student.score)
    """
    Suzuki 70
    Yamada 73
    Watanabe 88
    Tanaka 65
    """

print('\nSELECT all()')
for student in session.query(Student):  # .all() を省略
    print(student.name, student.score)
    """
    Suzuki 70
    Yamada 73
    Watanabe 88
    Tanaka 65
    """

print('\nSELECT one()')
student = session.query(Student).filter_by(name='Yamada').one()
print(student)  # <Student(id='5', name='Yamada', score='73')>

# 条件に一致するレコードがない場合は NoResultFound エラーになるので注意
print('\nSELECT No Result')
try:
    # sqlalchemy.orm.exc.NoResultFound: No row was found for one()
    student = session.query(Student).filter_by(name='Sato').one()
    print(student)
except NoResultFound as ex:
    print(ex)

print('\nSELECT get(id)')
student = session.query(Student).get(7)
print(student)  # <Student(id='7', name='Watanabe', score='88')>

print('\nSELECT get(id)')
student = session.query(Student).get(20)
print(student)  # None

print('\nORDER BY ... ASC')
for student in session.query(Student).order_by(Student.score.asc()):  # .asc() は省略可
    print(student.name, student.score)
    """
    Tanaka 65
    Suzuki 70
    Yamada 73
    Watanabe 88
    """

print('\nORDER BY ... DESC')
for student in session.query(Student).order_by(Student.score.desc()):  # 降順にするには .desc()
    print(student.name, student.score)
    """
    Watanabe 88
    Yamada 73
    Suzuki 70
    Tanaka 65
    """

# ページネーションで必須の LIMIT と OFFSET はスライス表記で指定
print('\nLIMIT and OFFSET')
for student in session.query(Student).order_by(Student.score.desc())[1:3]:
    print(student.name, student.score)
    """
    Yamada 73
    Suzuki 70
    """

# SQLAlchemy ではフィルターにより抽出条件を指定できます。（WHERE句に相当）
print('\nfilter ==')
for student in session.query(Student).filter(Student.name == 'Yamada'):
    print(student.name, student.score)
    """
    Yamada 73
    """

print('\nfilter !=')
for student in session.query(Student).filter(Student.name != 'Yamada'):
    print(student.name, student.score)
    """
    Suzuki 70
    Watanabe 88
    Tanaka 65
    """

print('\nfilter .like()')
# WHERE LIKE '%na%'
for student in session.query(Student).filter(Student.name.like('%na%')):
    print(student.name, student.score)
    """
    Watanabe 88
    Tanaka 65
    """

print('\nfilter AND (send multiple expressions to .filter())')
for student in session.query(Student).filter(Student.score > 70, Student.score < 80):
    print(student.name)
    """
    Yamada
    """

print('\nfilter AND - chain multiple filter()/filter_by() calls')
for student in session.query(Student).filter(Student.score > 70).filter(Student.score < 80):
    print(student.name)
    """
    Yamada
    """

# from sqlalchemy import or_
# for student in session.query(Student).filter(or_(Student.score < 70, Student.score > 80)):
# http://docs.sqlalchemy.org/en/latest/core/sqlelement.html#sqlalchemy.sql.expression.or_
print('\nfilter OR')
for student in session.query(Student).filter((Student.score < 70) | (Student.score > 80)):
    print(student.name)
    """
    Watanabe
    Tanaka
    """

# SELECT COUNT
# レコード数の取得
print('\ncount()')
count = session.query(Student).count()
print(count)  # 4

print('\ncount()')
count = session.query(Student).filter(Student.name.like('%na%')).count()
print(count)  # 2

##########
# UPDATE #
##########
student = session.query(Student).filter_by(name='Tanaka').one()
student.score = 75
session.add(student)
session.commit()

print('\nCheck for update')
student = session.query(Student).filter_by(name='Tanaka').one()
print(student)  # <Student(id='10', name='Tanaka', score='75')>

##########
# DELETE #
##########
# Delete one record
student = session.query(Student).get(10)
session.delete(student)
session.commit()

print('\nCheck for delete')
for student in session.query(Student):
    print(student.name)
    """
    Suzuki
    Yamada
    Watanabe
    """

# 全削除
session.query(Student).delete()
session.commit()

print('\nCheck for delete')
print(session.query(Student).count())  # 0

# クローズ
session.close()
