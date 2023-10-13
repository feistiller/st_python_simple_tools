import time

import pymysql
import datetime

conn = pymysql.connect(host="", user="", password="", database="",
                       charset="utf8",
                       port=3306,
                       autocommit=True)
cursor = conn.cursor()

# DB的存储结构见api.md
def select_data(sql):
    print(sql)
    cursor.execute(sql)
    return cursor.fetchall()


def save_data(sql):
    print(sql)
    cursor.execute(sql)
    conn.commit()


def get_luck_choice_users():
    sql = "select * from lucky where lucky = 0;"
    return select_data(sql)


def update_user_lucky(user_id, lucky_type):
    sql = " UPDATE `order_data`.`lucky` set `lucky` = " + str(
        lucky_type) + ", created_at='" + time.strftime(
        "%Y-%m-%d %H:%M:%S") + "' where id=" + str(user_id)
    return save_data(sql)


def get_lucky_users():
    sql = "select * from lucky where lucky>=1;"
    return select_data(sql)
