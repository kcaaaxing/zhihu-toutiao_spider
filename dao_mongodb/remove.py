import pymongo

# 连接(connect)
client = pymongo.MongoClient('localhost', 27017)
db = client['people']
collection = db['students']

# 删除(remove, 其他看书p221)
result = collection.remove({'name': 'Jordan'})
print(result)
