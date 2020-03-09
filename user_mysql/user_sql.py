import pymysql

"""
连接数据库需要用到的参数
主机：host
端口：port
用户名：user
密码：password
指定数据库：db
指定字符集：charset

"""
def mysql_get():
    # 打开数据库
    db = pymysql.connect(host='47.103.100.111',port=3306,user='root',password='789@456',database='chat-room')

    # 根据对象db，操纵cursor游标
    db.cursor()

    # 给cursor添加一个参数，让其的到数据是一个字典
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

    sql = """
    select * from t_user;
    """
    rows = cursor.execute(sql)
    print(rows)
    print(cursor.fetchone())
    print(cursor.fetchmany(5))

    ret = cursor.fetchall() # fetchall的作用就是获取所有行
    cursor.close()
    db.close()
    return ret


def forlist_user():
    list_user = mysql_get()
    for i in list_user:   # 遍历所有用户
        print(i)


if __name__ == '__main__':
    forlist_user()
