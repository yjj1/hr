# -*- coding:'utf8' -*-
#encoding=utf-8

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from orm import ResumeBaseInfo
class ConnectDb:
    db_session = None

    def __init__(self):
        db_url = 'mysql+pymysql://root:test@localhost:3306/hr?charset=utf8'
        engine = create_engine(db_url, echo=True)
        # metaData=MetaData(engine)
        DBSession = sessionmaker(bind=engine)
        self.db_session = DBSession()
        #
        # spiderData = self.db_session.query(ResumeBaseInfo).one()
        # print spiderData.resumeCode

if __name__ == '__main__':
    connect = ConnectDb()