import pymysql
import requests

"""

华为app软件评论爬虫
"""
class Database:
    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'root'
        self.password = '123456'
        self.db = 'flask'
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute(self, sql, params=None):
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            self.conn.rollback()
            self.close()
            return False

    def execute_many(self, sql, values):

        try:
            self.cursor.executemany(sql, values)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            self.conn.rollback()
            self.close()
            return False

    def fetchall(self, sql, params=None):
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            result = self.cursor.fetchall()
            fields = [field[0] for field in self.cursor.description]
            # 序列化 成字典 zip  把两个可迭代对象合并成2维元组。然后用dict 转化为字典。
            res = [dict(zip(fields, result)) for result in result]

            return res
        except Exception as e:
            print(e)
            self.close()
            return None
# 获取爬虫信息地址： https://appgallery.huawei.com/app/C5373

# 爱奇艺： https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.user.commenList3&serviceType=20&reqPageNum=3&maxResults=25&appid=C2002&version=10.0.0&zone=&locale=zh

# 抖音： https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.user.commenList3&serviceType=20&reqPageNum=1&maxResults=25&appid=C10652857&version=10.0.0&zone=&locale=zh


# 微信： https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.user.commenList3&serviceType=20&reqPageNum=1&maxResults=25&appid=C5683&version=10.0.0&zone=&locale=zh

# qq: https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.user.commenList3&serviceType=20&reqPageNum=1&maxResults=25&appid=C9319&version=10.0.0&zone=&locale=zh

# 支付宝： https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.user.commenList3&serviceType=20&reqPageNum=1&maxResults=25&appid=C5373&version=10.0.0&zone=&locale=zh

for j in range(1, 5):

    software_name = "支付宝"

    res = requests.get(url=f"https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.user.commenList3&serviceType=20&reqPageNum={j}&maxResults=25&appid=C5373&version=10.0.0&zone=&locale=zh")

    comment_list = res.json()["list"]
    data = []
    for i in comment_list:
        commentInfo = i["commentInfo"]
        stars = i["stars"]
        if stars == "5":
            comment_type = "好评"
        else:
            comment_type = "差评"

        data.append((software_name, commentInfo, stars, comment_type))


    db = Database()

    print(data)
    sql = """
    insert into comment (name, info, stars, comment_type) values (%s,%s,%s,%s);
    """

    db.execute_many(sql, data)


    db.close()

