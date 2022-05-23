# generate url from database
from configure.settings import DBSelector

class DataSource():

    def __init__(self):
        self.db= DBSelector().get_mysql_conn('daydo',type_='local')


    def urls(self):
        
