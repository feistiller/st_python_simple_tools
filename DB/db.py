import pymysql

db = pymysql.connect(
    host="127.0.0.1", user="root", password="root", database="db",
    charset="utf8",
    port=3306,
    autocommit=True
)


def insert_sql(sql):
    print(sql)
    cursor = db.cursor()  # 创建游标对象
    cursor.execute(sql)  # 执行sql语句
    cursor.close()

# db.close()  # 关闭数据库的连接
