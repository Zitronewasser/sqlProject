import requests
import sqlite3

# 从 Zentao 下载数据的函数
def fetch_data_from_zentao():
    api_url = 'https://your.zentao.api/endpoint'  # 替换为你的 Zentao API 端点
    response = requests.get(api_url)
    data = response.json()
    return data

# 将数据插入数据库的函数
def insert_data_into_db(data):
    conn = sqlite3.connect('zentao_bugs.db')
    cursor = conn.cursor()

    for bug in data:
        cursor.execute('''
        INSERT INTO bugs (product_name, bug_status, keywords, image_url)
        VALUES (?, ?, ?, ?)
        ''', (bug['product_name'], bug['bug_status'], bug['keywords'], bug['image_url']))

    conn.commit()
    conn.close()

# 主程序
if __name__ == "__main__":
    data = fetch_data_from_zentao()
    insert_data_into_db(data)
    print("Data fetched and stored successfully.")