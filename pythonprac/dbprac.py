from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# doc = {'name': 'jane', 'age': 21}  # 딕셔너리 만듬
# db.users.insert_one(doc)  # db -> users에 넣음


# same_ages = list(db.users.find({'age': 21}, {'_id': False}))
# # same_ages = list(db.users.find({}, {'_id': False})) ## 모든 걸 find 할 때 빈 중괄호
# # print(same_ages)

# for person in same_ages:
#     print(person['name'])

# user = db.users.find_one({'name': 'bobby'}, {'_id': False})
# print(user['age'])


# db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})  # 업데이트

# db.users.update_many({'name': 'bobby'}, {'$set': {'age': 19}})  # 업데이트name이 bobby인 애들 모두 19로 바꿈

# db.users.delete_one({'name': 'bobby'})

########################################
# 저장 - 예시
doc = {'name': 'bobby', 'age': 21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name': 'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age': 21}, {'_id': False}))

# 바꾸기 - 예시
db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})

# 지우기 - 예시
db.users.delete_one({'name': 'bobby'})
