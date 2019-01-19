# coding: utf-8
# author: hmk

from commonlib.readconfig import ReadConfig
import pymysql.cursors


class HandleMysql:
    def __init__(self):
        self.data = ReadConfig()

    def conn_mysql(self):
        """连接数据库"""
        host = self.data.get_db("host")
        user = self.data.get_db("user")
        password = self.data.get_db("password")
        db = self.data.get_db("db")
        charset = self.data.get_db("charset")
        try:
            self.conn = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
            self.cur = self.conn.cursor()
        except BaseException as e:
            raise  e
            #print("Mysqldb Error:%s" % e)
    def execute_sql(self, sql, data=None):
        try:
            """执行操作数据的相关sql"""
            self.conn_mysql()
            self.cur.execute(sql, data)
            self.conn.commit()
        except BaseException as e:
            self.conn.rollback()
            print("Mysqldb Error:%s" % e)
    def search(self, sql,data=None):
        """执行查询sql"""
        self.conn_mysql()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def close_mysql(self):
        """关闭数据库连接"""
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    test = HandleMysql()
    test.conn_mysql()
    sql = "select * from wyqtest1"
    yy=test.execute_sql(sql)
    print(yy)
    test.close_mysql()