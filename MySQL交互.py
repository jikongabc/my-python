import pymysql
# 1. 连接数据库
db = pymysql.connect(
    host="localhost",
    user="root",
    password="a2c4e6g8",
    database="jikong"
)
# 2. 创建一个数据库游标对象
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

sql = "select * from user_login"

cursor=pymysql.cursors.DictCursor

res = cursor.execute(sql)
print(res)

print(cursor.fetchall())
print(cursor.fetchone())
print(cursor.fetchmany(2))
print(cursor.fetchmany(4))


print(cursor.fetchone())
cursor.scroll(1, 'relative')
print(cursor.fetchone())
cursor.scroll(2, 'absolute')
print(cursor.fetchone())

# 登录交互
user_name = input('name:')
password = input('password:')

sql = "select * from user_login where username=%s and password=%s"

print('sql>>>>', sql)

res = cursor.execute(sql, (user_name, password))

if res:
    print('登录成功')
else:
    print('登录失败')

# 事务
db.begin()

try:
    sql1 = "insert into user_login(username,password) values('张三', '123')"
    res1 = cursor.execute(sql1)
    sql2 = "insert into user_login(username,password) values('李四', '456')"
    res2 = cursor.execute(sql2)
    db.commit()
except Exception as e:
    db.rollback()
    print('事务执行失败：', e )



