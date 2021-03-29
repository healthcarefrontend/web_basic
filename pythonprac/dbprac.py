from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# doc = {'name': 'jane', 'age': 21}  # 딕셔너리 만듬
# db.users.insert_one(doc)  # db -> users에 넣음


same_ages = list(db.users.find({'age': 21}, {'_id': False}))
# same_ages = list(db.users.find({}, {'_id': False})) ## 모든 걸 find 할 때 빈 중괄호
# print(same_ages)

for person in same_ages:
    print(person['name'])

#insert / find / update / delete
