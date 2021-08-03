from DataBase import DataBase
from datetime import datetime
import json


class User():

    # 创建实例后先创建数据库访问工具 userId为微信的openid
    def __init__(self, userId):
        self.userId = userId
        self.db = DataBase()
        self.userInit()

    # 初始化用户信息，若不存在，则创建用户
    def userInit(self):
        sql = "select * from users where user_id = '{userId}'".format(userId = self.userId)
        r = self.db.query(sql)
        if len(r) == 0:
            current_time = datetime.now()
            insert = "insert into users value ('{userId}','{reg_time}','{last_time}')".format(userId = self.userId, reg_time = current_time, last_time = current_time)
            print(insert)
            r = self.db.execute(insert)

    # 获取用户最后一次登录时间
    def getLastTime(self):
        sql = "select * from users where user_id = '{userId}'".format(userId = self.userId)
        r = self.db.query(sql)
        return str(r[0]['last_time'])

    # 获取用户访问真题权限
    def getTopicPower(self):
        sql = "select * from activition_code where user_id = '{userId}' and used = '1' and used_time < DATE_ADD(used_time, INTERVAL 1 YEAR) ".format(userId = self.userId)
        r = self.db.query(sql)
        if len(r) == 0:
            return 0
        else:
            topic_power = {}
            for i in r:
                topic_type = i['topic_type']
                topic_power[topic_type] = str(i['used_time'])
            return topic_power

    # 获取相关用户信息以Json的方式 
    def getUserInfoToJson(self):

        # 获取用户基本信息(上次登录时间、微信OpenId)
        last_time = self.getLastTime()
        base = {'open_id' : self.userId,'last_time': last_time}

        # 获取用户权限信息
        power = self.getTopicPower()

        userInfo = [base,power]

        userInfoToJson = json.dumps(userInfo, ensure_ascii = False)
        
        return userInfoToJson


user = User('456')
r = user.getUserInfoToJson()
print(r)
