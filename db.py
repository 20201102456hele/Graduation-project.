import pymysql


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


if __name__ == '__main__':
    db = Database()

    create_user_sql = """
        CREATE TABLE  if not exists `51job`.`Untitled`  (
      `name` varchar(255) NULL,
      `password` varchar(255) NULL,
      `id` int NOT NULL AUTO_INCREMENT
    );

    """

    db.execute(create_user_sql)

    db.close()






















