from pymongo import MongoClient


client = MongoClient('localhost', 27017)

mydb = client['table2']
mycol = mydb['table2']

for col in mycol.find({"num":{"$gt":1}}):
    print(col)
