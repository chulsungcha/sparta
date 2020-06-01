from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      
 
# target = db.movies.find_one({'title':'매트릭스'})
# target_star = target['star']

# targets = list(db.movies.find({'star':target_star},{'_id':False}))
# print(targets)

# for movie in targets:
#     print(movie['title'])

target = db.movies.find_one({'title':'매트릭스'})
target_star = target['star']

db.movies.update_many({'star':target_star},{'$set':{'star':0}})
