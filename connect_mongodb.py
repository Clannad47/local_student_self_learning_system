import pymongo
from loguru import logger
import pytz
import datetime
import os

tz = pytz.timezone('Asia/Shanghai')
log_time = datetime.datetime.now()
log_time_eastern = log_time.astimezone(tz)
logger.remove()  
log_time_str = log_time.strftime("%Y%m%d")
log_file_path=f"./log/mongodb/app_{log_time_str}.log"
log_directory = os.path.dirname(log_file_path)
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
logger.add(log_file_path,format="{time} | {level}     | {process}-{thread} |{file}:{function}:{line} - {message}")

class Mongodb:
    def __init__(self):
        client = pymongo.MongoClient("mongodb://root:root@localhost:27017")
        db = client["user"]
        self.collection = db["user"]
        self.user=[]

    def InsertOne(self,user):
        try:
            insert_result = self.collection.insert_one(user)
            logger.info(f"插入数据的 ID：{insert_result.inserted_id}")
            logger.info(f"插入的数据 ：{insert_result}")
        except:
            logger.debug(f'插入数据失败,数据id {insert_result.inserted_id}')
        
    def FindAll(self):
        self.user=[]
        documentation=self.collection.find()
        for doc in documentation:
            if doc.get('username'):
                self.user.append(doc)
        return self.user
    def Find(self,prompt):
        query = {'$or': [{'username': prompt}, {'password': prompt}]}
        try:
            res=self.collection.find_one(query)
        except:
            logger.info(f"查询失败,查询的输入记录：{prompt}")

        return res

    def UpdateByName(self,prompt,password):
   
        try:
            update_result = self.collection.update_one({"username":prompt }, {"$set": {"password": password}})
            logger.info(f"更新文档： {update_result}")
        except:
            logger.info(f'更新失败,原数据 {self.collection.find(prompt)}')

            
        
    def check_login(self,username,password):
        self.FindAll()
        for user in self.user:
            if username == user['username'] and password == user['password']:
                return True
        return False

    def RemoveByName(self,name):
        try:
            self.collection.delete_one({"username": name})
        except:
            logger.info(f'删除失败,数据 {self.collection.find(name)}')


if __name__=='__main__':
    
    mongodb=Mongodb()


    ans=mongodb.Find('123')
    print(mongodb.FindAll())


