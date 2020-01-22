import pymysql as db


class Mydb:

    def __ready(self):
        self.__con = db.connect(
            host='localhost',
            user='wwj',
            password='toor',
            database='w_blog',
            charset='utf8')
        self.__cursor = self.__con.cursor()

    def __close(self):
        self.__con.close()
        self.__cursor.close()

    def getUserPasswd(self, username):
        self.__ready()
        sql = 'select u_passwd from b_user where u_name=%s'
        self.__cursor.execute(sql, [username])
        self.__con.commit()
        rs = self.__cursor.fetchall()
        self.__close()
        print(rs)
        if rs:
            # return None
            print(rs[0])
            print(rs[0][0])
            print(type(rs[0][0]))
            return rs[0][0]
        else:
            return None

    def getUserPasswd1(self, username):
        sql = "select u_passwd from b_user where u_name = '{}'".format(username)
        print(sql)
        cursor = self.con.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        print(rs)
        for i in rs:
            print(i)
        cursor.close()

    def addPost(self, p_title, p_content, p_datetime):
        self.__ready()
        sql = 'insert into b_post(p_title, p_content, p_datetime) values (%s,%s,%s)'
        self.__cursor.execute(sql, [p_title,p_content,p_datetime])
        self.__con.commit()
        rs = self.__cursor.fetchall()
        self.__close()
        print(rs)
        return 1

    def getPost(self, startPage, pageCount):
        self.__ready()
        sql = 'select * from b_post limit %s, %s'
        self.__cursor.execute(sql,(startPage,pageCount))
        self.__con.commit()
        rs = self.__cursor.fetchall()
        self.__close()
        print(rs)
        rs_list = []
        j = 0
        for row in rs:
            temp = {}
            temp['p_title'] = row[1]
            temp['p_content']=row[2]
            print(type(row[3]))
            print(row[3].strftime("%Y-%m-%d %H:%M:%S"))
            temp['p_datetime']=row[3].strftime("%Y-%m-%d %H:%M:%S")
            print(temp)
            rs_list.append(temp)
        print(rs_list)

        return rs_list

    def getPostCount(self):
        self.__ready()
        sql = 'select count(*) from b_post'
        self.__cursor.execute(sql)
        self.__con.commit()
        rs = self.__cursor.fetchall()
        self.__close()
        print(rs[0][0])
        return rs[0][0]

if __name__ == '__main__':
    aa = Mydb()
    # aa.getPost(0, 5)
    aa.getPostCount()
    # aa.getUserPasswd('wwj')
    # if None:
    #     print('ke')
    # else:
    #     print('dd')
    # db.getUserPasswd1('wwj')
