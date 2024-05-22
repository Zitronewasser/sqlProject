import sqlite3

# 创建一个数据库连接
conn = sqlite3.connect('zentao_bugs.db')

# 创建一个游标对象
cursor = conn.cursor()

# 创建一个表
cursor.execute('''
CREATE TABLE IF NOT EXISTS bugs (
    id INTEGER PRIMARY KEY,
    product_name TEXT,
    bug_status TEXT,
    keywords TEXT,
    image_url TEXT
)
''')

# 提交更改并关闭连接
conn.commit()
conn.close()

print("Database and table created successfully.")