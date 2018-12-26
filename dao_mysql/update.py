import pymysql


data = {
    'id': '20190007',
    'name': 'CeT',
    'age': 21
}
table = 'people'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'insert into {table}({keys}) values ({values})' \
      ' on duplicate key update'.format(table=table, keys=keys, values=values)
update = ','.join([' {key} = %s'.format(key=key) for key in data])
sql += update
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='cy_my_data')
cursor = db.cursor()

print(sql)
print(tuple(data.values())*2)

try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
