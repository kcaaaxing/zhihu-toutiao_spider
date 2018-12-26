from redis import StrictRedis

# 连接(connect, 其他连接方法看p222)
# 没有安装RedisDump
redis = StrictRedis(host='localhost', port=6379, db=0)
redis.set('name', 'Bob')
print(redis.get('name'))
