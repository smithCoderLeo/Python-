# 建立report表，存储内容
import os, subprocess, sqlite3
import pandas as pd
import numpy as np

report_dir =
db = 

# 获取数据库连接
def open_db():
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor() # 命令中枢
        print('数据库连接成功！')
        print(' ')
        return conn, cur
    except:
        print('数据库连接失败')


def insert_report_data(fields, values):
    # 插入时候列名特别清楚，但是id必须要设置为自增
    # 插入数据时，必须要使用元组类型
    s = ','.join('?' for _ in range(len(values)))
    sql = "insert into intezer_report {} values ({})".format(fields, s)
    conn, cur = open_db()
    cur.execute(sql, values)
    conn.commit()
    cur.close()
    conn.close()

def delete_score_data():
    # 1、获取连接
    conn, cur = sqlite3.connect(db)
    # 删除语句 delete from + 表名 where 列=？
    sql = "delete from intezer_report where id=?"

def query_data():
    sql = "select * from intezer_report"
    cur = open_db()
    conn,cur = cur.execute(sql)
    print(cur.fetchall())
    conn.close()

# 修改数据，根据条件修改数据
def update_data():
    conn, cur = open_db()
    sql = "update intezer_report set Family = ? where id = "



for root, dirs, files in os.walk(dir):
    for file in files:
        abs_path = os.path.join(root, file)
        df = pd.read_csv(abs_path, header=0, encoding='utf-8')
        fields = ()
        for row in df.values:
            row = tuple(row)
            insert_report_data(fields, row)



