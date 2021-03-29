from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

matrix = db.movies.find_one({'title': '매트릭스'})
matrix_star = matrix['star']

# for moive in movies:
#     print(movie)


movies_list = list(db.movies.find({}, {'_id': False}))
# print(movies['star'])

for movie in movies_list:
    if movie['star'] == matrix_star:
        print(movie['title'])


# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# same_ages = list(db.users.find({'age': 21}, {'_id': False}))

# # 바꾸기 - 예시
# 0은 숫자 '0' 문자열로 바꿔줌
db.movies.update_one({'title': '매트릭스'}, {'$set': {'star': '0'}})

# # 지우기 - 예시
# db.users.delete_one({'name': 'bobby'})
