import pymysql


db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='cy_my_data')
cursor = db.cursor()
sql = 'create table if not exists people (id varchar(255) not null, name varchar(255) not null, age int not null,' \
      'primary key (id))'
cursor.execute(sql)
db.close()
