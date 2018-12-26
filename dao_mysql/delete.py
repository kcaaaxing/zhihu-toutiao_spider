import pymysql


table = 'people'
condition = 'age > 30'

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='cy_my_data')
cursor = db.cursor()
sql = 'delete from {table} where {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    print('失败')
    db.rollback()

db.close()
