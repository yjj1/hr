# -*- coding:'utf8' -*-
#encoding=utf-8

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from orm import ResumeBaseInfo
global connect
class ConnectDb(object):
    db_session = None
    __instance = None
    def __init__(self):
        pass

    def initDb(self):
        db_url = 'mysql+pymysql://root:test@localhost:3306/hr?charset=utf8'
        engine = create_engine(db_url, echo=True)
        # metaData=MetaData(engine)
        DBSession = sessionmaker(bind=engine)
        self.db_session = DBSession()

    def __new__(cls, *args, **kwargs):
        if ConnectDb.__instance is None:
            ConnectDb.__instance = object.__new__(cls, *args, **kwargs)
            ConnectDb.__instance.initDb()
        return ConnectDb.__instance

if __name__ == '__main__':
    connect = ConnectDb()