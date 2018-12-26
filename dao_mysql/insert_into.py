import pymysql


data = {
    'id': '20120006',
    'name': 'CdF',
    'age': 32
}
table = 'people'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'insert into {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='cy_my_data')
cursor = db.cursor()

# 验证
print(data.keys())
print(data.values())

try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()

db.close()
