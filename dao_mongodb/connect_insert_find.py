import pymongo
from bson.objectid import ObjectId

# 连接(connect)
client = pymongo.MongoClient('localhost', 27017)
db = client['people']
collection = db['students']

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

# 插入(insert_one, insert_many)
result = collection.insert_many([student1, student2])
print(result)
print(result.inserted_ids)

# 查询(find)
print('---------------------------------------------')
result = collection.find_one({'name': 'Mike'})
print(type(result))
print(result)

# 根据ObjectId来查询
result = collection.find_one({'_id': ObjectId('5c0bdf021721ed16cc6d3079')})
print(result)

# 查询多条数据
results = collection.find({'age': 21})
print(results)  # 返回的是Cursor类型,它相当于一个生成器
for r in results:
    print(r)

# 查询年龄大于20的数据
results = collection.find({'age': {'$gt': 20}})
print('###########################################')
print(results)
for r in results:
    print(r)

# 进行正则匹配查询,其他操作看书p218
results = collection.find({'name': {'$regex': '^M.*'}})
print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
print(results)
for r in results:
    print(r)
