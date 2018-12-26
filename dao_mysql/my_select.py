import pymysql


sql = 'SELECT * FROM people where age >= 20'
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='cy_my_data')
cursor = db.cursor()
print(db)
try:
    if cursor.execute(sql):
        print('success')
        print('Count:', cursor.rowcount)
        results = cursor.fetchall()
        print('Results:', results)
        print(type(results))
        for row in results:
            print(row)
except:
    print('False')
    db.rollback()
db.close()
