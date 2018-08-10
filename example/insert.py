from pymongo import MongoClient


client = MongoClient('localhost', 27017)

mydb = client['table2']
mycol = mydb['table2']

mydict = {"name": "aaa", "num": 4, "age": 4}

x = mycol.insert_one(mydict)


