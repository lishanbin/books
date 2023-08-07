from pymysql import connect
from pymysql.cursors import DictCursor
from settings import MYSQL_HOST,MYSQL_PORT,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DATABASE


class Book(object):
    def __init__(self) -> None:
        self.conn = connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            charset='utf8'
        )
        self.cursor = self.conn.cursor(DictCursor)

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_books_infos_limit(self):
        sql = 'select * from book_infos limit 1'
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data;

    def get_cates_newest_books_30(self,book_cate):
        sql = 'select id,book_id,book_name,book_last_update_time, \
            book_newest_name,book_newest_url from book_infos \
            where book_cate="{}" order by book_last_update_time desc limit 30'.format(book_cate)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data;

    def get_cates_most_books_30(self,book_cate):
        sql = 'select id,book_id,book_name,book_last_update_time, \
            book_author from book_infos \
            where book_cate="{}" order by book_newest_url desc limit 30'.format(book_cate)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data;

    def get_book_infos_by_book_id(self,book_id):
        sql = "select * from book_infos where book_id='{}'".format(book_id)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data;

    def get_book_details_by_book_id(self,book_id):
        sql = "select * from book_details where book_id='{}' order by sort_id".format(book_id)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data;

    def get_book_details_newest_20_by_book_id(self,book_id):
        sql = "select * from book_details where book_id='{}' order by sort_id desc limit 20".format(book_id)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data;




    