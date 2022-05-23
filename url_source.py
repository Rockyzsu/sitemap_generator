# generate url from database
from configure.settings import DBSelector
HOST='http://www.30daydo.com/' # 写入你的网站域名

class DataSource():

    def __init__(self):
        self.db= DBSelector().get_mysql_conn('daydo',type_='local')
        self.cursor = self.db.cursor()

    def urls(self):
        return self.articles()+self.questions()

    def articles(self):
        cmd = 'select id from `aws_article`'
        self.cursor.execute(cmd)
        ret = self.cursor.fetchall()
        result=[]
        for i in ret:
            result.append(HOST+'article/'+str(i[0])) # 拼接完整路径
        return result

    def questions(self):
        cmd = 'select question_id from `aws_question`' 
        self.cursor.execute(cmd)
        ret = self.cursor.fetchall()
        result=[]
        for i in ret:
            result.append(HOST+'question/'+str(i[0])) # 拼接完整路径
        return result

    def run(self):
        return self.urls()