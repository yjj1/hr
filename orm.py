# -*- coding:'utf8' -*-
#encoding=utf-8

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EmailOrm(Base):

    __tablename__   = 'origin_email'

    emailId = Column(String(50), primary_key=True)
    emailName = Column(String(50))
    sendDate = Column(String(50))
    receiveDate = Column(String(50))
    fromWho = Column(String(50), name='from')
    toWho = Column(String(50), name='to')
    size = Column(String(50))
    report = Column(String(50))
    isread = Column(String(50))
    priority = Column(String(50))

    def __init__(self, id):
        self.emailId = id

class ResumeApply(Base):

    __tablename__   = 'resume_apply'

    applyId = Column(String(50), primary_key= True)
    applier = Column(String(50))
    resumeId = Column(String(50))
    applyDate = Column(String(50))

    def __init__(self, id):
        self.applyId = id

class ResumeBaseInfo(Base):

    __tablename__   = 'resume_base_info'

    resumeId = Column(String(50), primary_key=True)
    resumeCode = Column(String(50))
    name = Column(String(50))
    sex = Column(String(50))
    birthday = Column(String(50))
    eduBack = Column(String(50))
    eduDegree = Column(String(50))
    school = Column(String(50))
    phone = Column(String(50))
    homePhone= Column(String(50))
    resumePath = Column(String(100))
    politicsStatus = Column(String(50))
    nativePlace = Column(String(50))
    address = Column(String(100))
    bigBang = Column(String(200))
    height = Column(String(50))
    healthy = Column(String(50))
    marriage = Column(String(50))
    idCard = Column(String(50))
    job = Column(String(50))
    isAddressControl = Column(String(50))

    def __init__(self, id):
        self.resumeId = id

class Edu(Base):

    __tablename__   = 'edu'

    eduId = Column(String(50), primary_key=True)
    resumeId = Column(String(50))
    eduType = Column(String(50))
    schoolName = Column(String(100))
    eduDate = Column(String(50))
    eduPro = Column(String(50))
    # remark = Column(String(50))

    def __init__(self, id):
        self.eduId = id

class Family(Base):

    __tablename__   = "family"

    familyId = Column(String(50), primary_key=True)
    resumeId = Column(String(50))
    relationShip = Column(String(50))
    name = Column(String(50))
    politicsStatus = Column(String(50))
    company = Column(String(50))
    job = Column(String(50))

    def __init__(self, id):
        self.familyId = id