import pymysql


class DataBase():
    def __init__(self):
        self._conn = pymysql.connect(host='39.99.229.107',port=3306, user='root', password= 'root', database='examsytem', charset='utf8')
        self._curs = self._conn.cursor(pymysql.cursors.DictCursor)

    # 查询结果是一个list，list中每个元素是一个dict
    def query(self, sql):
        self._curs.execute(sql)
        result=self._curs.fetchall() 
        return result

    def execute(self, sql):
        self._curs.execute(sql)
        self._conn.commit()
        result = self._curs.rowcount
        return result

    def close(self):
        self._curs.close()
        self._conn.close()
