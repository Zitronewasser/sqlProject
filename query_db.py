import sqlite3

# 查询数据库的函数
def query_db():
    conn = sqlite3.connect('zentao_bugs.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM bugs')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

# 主程序
if __name__ == "__main__":
    query_db()