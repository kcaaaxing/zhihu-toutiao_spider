import pymongo

# 连接(connect)
client = pymongo.MongoClient('localhost', 27017)
db = client['people']
collection = db['students']

# 更新(update, 其他看书p220)
condition = {'name': 'Jordan'}
student = collection.find_one(condition)
student['age'] = 26
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)
