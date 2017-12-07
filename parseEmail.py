# -*- coding:'utf8' -*-
#encoding=utf-8

import urllib
import urllib2

import os
import uuid

import requests
import time
from bs4 import BeautifulSoup

from connect_db import ConnectDb
from orm import TempEmail, OriginEmail, Accessory
import sys

from parseDoc import ParseDoc

defaultencoding = 'utf-8'
from urllib import urlencode
import json
import util
#login email
#if need vefiry code
# def assignKey(o, e):
#     if o.attrs['name'] == 'id':
#         e = EmailOrm(o.string)
#     elif o.attrs['name'] == 'subject':
#         e.emailName = o.string
#     # elif o.attrs['name'] ==

class Email:
    username = None
    password = None
    url11 = 'http://mail.163.com/js6/main.jsp?sid=uCJoJpaaVDscennkuFaajkNAtqpTNdHs&df=email163'
    login_url = 'https://mail.163.com/entry/cgi/ntesdoor?funcid=loginone&language=-1&passtype=1&iframe=1&product=mail163&from=web&df=email163&race=25_10_29_bj&module=&uid=qh4343222tuxizhen@163.com&style=-1&net=n&skinid=null'
        #'http://mail.163.com/entry/cgi/ntesdoor?'
    host_url = 'mail.163.com'
    origin = 'http://email.163.com'
    refer = 'http://email.163.com'
    receiveUrl = None
    receiveXml = None
    sid = None
    header = None
    session = None
    db_session = None

    def encryPwd(self, p):
        self.password = p

    #请求s页面获取邮箱页面的json内容,为了确定附件的文件个数
    def preJsonInfo(self, e):
        url = 'https://mail.163.com/js6/s?sid=' \
              + self.sid \
              + '&func=mbox:readMessage&mbox_folder_enter=1&l=read&action=read'
        xml = '<?xml version="1.0"?><object><string name="id">' \
              + e.emailId + \
              '</string><boolean name="header">true</boolean><boolean name="returnImageInfo">true</boolean><boolean name="returnAntispamInfo">true</boolean><boolean name="autoName">true</boolean><object name="returnHeaders"><string name="Resent-From">A</string><string name="Sender">A</string><string name="List-Unsubscribe">A</string><string name="Reply-To">A</string></object><boolean name="supportTNEF">true</boolean></object>'
        data = {
            'var' : xml
        }
        print url
        s = urlencode(data).replace('+', '%20')
        self.header['Accept'] = 'text/json'
        self.header['Referer'] = 'https://mail.163.com/js6/main.jsp?' \
                                 'sid=bCywIHXXIULFKCzWmPXXWgykOUOuwYoX&df=mail163_letter'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        resp = self.session.post(url, data=s, headers = self.header)
        result = resp.content
        result = result.replace('\n', '')
        # result = result.replace('\'','\"')
        # datas = util.trans_xml_to_dict(result)
        xml = BeautifulSoup(result)
        object = xml.find_all('object')
        i = 0
        j = 3
        for obj in object:
            if i > 5:
                for o in obj:
                    if o.attrs['name'] == 'filename':
                        name = o.string
                        self.downloadDoc(e, str(j), name)
                        j = j + 1
            i = i + 1

            # print result

        # str = json.dumps(result, ensure_ascii=False)
        # # str = str.replace('\n','')
        # js = json.loads(str, encoding='utf-8')
        # s = '{\"code\":\"ok\"}'
        # jss = json.dumps(s)
        # j_jss = json.loads(jss)
        # print j_jss['code']

    def downloadDoc(self, e, part, name):
        url = 'https://mail.163.com/js6/read/readdata.jsp?mid=' + e.emailId + '&sid=' + self.sid
        url = url + '&mode=download&l=read&action=download_attach&part=' + part
        resp = self.session.post(url, headers=self.header)

        name = 'D:\\hr_file\\'+str(uuid.uuid4()) + name
        with open(name, "wb") as code:
            code.write(resp.content)
        # 保存附件
        accessory = Accessory(str(uuid.uuid4()))
        accessory.emailId = e.emailId
        accessory.path = name
        #if file is doc, parse it
        suffix = os.path.splitext(name)[1]
        if suffix == '.doc' and e.status == '0':
            try:
                parse = ParseDoc()
                parse.setEmailId(e.emailId)
                parse.parse(name)
            except:
                self.db_session.query(OriginEmail)\
                    .filter(OriginEmail.emailId==e.emailId)\
                    .update({
                    OriginEmail.status : '-1'
                })
                self.db_session.commit()

    def parsePerEmail(self, e):
        url = 'https://mail.163.com/js6/read/readhtml.jsp?mid='+ e.emailId + '&sid=' + self.sid

        data = {
            'sid': self.sid,
            'mid': e.emailId,
            'font': '15',
            'color': '064977'
        }

        resp = self.session.post(url, data, self.header)
        resp_header = resp.headers
        encode_type_str = resp_header['Content-Type']
        encode_type = encode_type_str.split('charset=')[1]
        print url
        print resp.content.decode(encode_type)
        self.preJsonInfo(e)

    def goToReceiveHtml(self, sid):
        url = 'http://mail.163.com/js6/s?' \
              'sid=' + sid + \
              '&func=mbox:listMessages' \
              '&welcome_welcomemodule_mailrecom_click=1' \
              '&mbox_folder_enter=1'
        self.receiveUrl = url
        return url

    #解析收件箱xml
    #当前页邮件,当前页码,总页码
    #TODO 下一页
    def parseReceiveXml(self):
        xml = self.receiveXml.replace('\n', '')
        soup = BeautifulSoup(xml)
        array = soup.result.array
        # for obj in array:
        #     print obj.content
        objects = array.find_all('object')
        list = []
        for obj in objects:
            e = None
            for o in obj:
                print o.string,':', o.attrs['name']
                if o.attrs['name'] == 'id':
                    e = OriginEmail(o.string)

                if o.attrs['name'] == 'subject':
                    e.emailName = o.string

                if o.attrs['name'] == 'size':
                    e.size = o.string

                if o.attrs['name'] == 'from':
                    e.fromWho = o.string

                if o.attrs['name'] == 'to':
                    e.toWho = o.string

                if o.attrs['name'] == 'sentDate':
                    e.sendDate = o.string

                if o.attrs['name'] == 'receiveDate':
                    e.receiveDate = o.string

                if o.attrs['name'] == 'priority':
                    e.priority = o.string

                # if o.attrs['name'] == 'read':
                #     e.isread = o.string

            if e != None:
                list.append(e)

        return list

    def login(self):
        session = requests.Session()
        cookie = {
            'starttime', time.time(),
            'df', 'mail163_letter'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/61.0.3163.100 Safari/537.36',
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": self.host_url,
            "Origin": self.origin,
            "Refer": self.refer
        }

        # data = {
        #     'un':self.username,
        #     'pw':self.password,
        #     't':'1512109043219',
        #     'domains':'163.com',
        #     'd':'10',
        #     'pkid':'CvViHzl',
        #     'topURL':'http%3A%2F%2Fmail.163.com%2F',
        #     'l':'0',
        #     'pwdKeyUp':'1',
        #     'tk':'2b231bd5bf303ce4310a05cd440a3afc'
        # }
        # data = {
        #     'passtype':'1',
        #     ''
        # }

        gOption = {
            "sDomain": "163.com",
            "sCookieDomain": "mail.163.com",
            "sAutoLoginUrl": "http://mail.163.com/entry/cgi/ntesdoor?lightweight=1&verifycookie=1&language=-1&from=web&df=webmail163",
            "sSslAction": "https://mail.163.com/entry/cgi/ntesdoor?",
            "product": "mail163",
            "url": "http://mail.163.com/entry/cgi/ntesdoor?",
            "url2": "http://mail.163.com/errorpage/error163.htm",
            "gad": "mail.163.com"
        }

        oParam = {
            'df':'mail163_letter',
            'language': '-1',
            'from': 'web',
            'iframe': '1',
            'savelogin': '0',
            'passtype': '1',
            'product':'mail163',
            'url2':gOption["url2"],
            'email':'15258297577@163.com',
            'uid':'15258297577@163.com',
            'username':'15258297577@163.com',
            'password':'martha3137',
        }
        resp = session.post(self.login_url, headers=headers, data=oParam)

        soup = BeautifulSoup(resp.content)
        s = soup.script.string
        s = s.split('\"')[1]
        respCookie = resp.cookies
        sCookie = ''
        for c in respCookie:
             sCookie = sCookie + c.name + '='+ c.value + ';'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/61.0.3163.100 Safari/537.36',
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": self.host_url,
            "Origin": self.origin,
            "Refer": self.login_url,
            'Cookie': sCookie,
            'Content-Type': 'utf8'
        }
        #登录成功后的sid即为带有登录session的标识码，是邮箱唯一身份识别码
        sid = s.split('&')[0]
        sid = sid.split('=')[1]
        print sid
        self.sid = sid

        #通过sid组装收件箱地址
        receiveHtml = self.goToReceiveHtml(sid)
        resp = session.post(receiveHtml)

        self.receiveXml = resp.content
        list = self.parseReceiveXml()
        self.header = headers
        self.session = session

        # e = list[1]
        # data1 = {
        #     'sid': self.sid,
        #     'mid': e.emailId,
        #     'font': '15',
        #     'color': '064977'
        # }
        #
        # url = 'https://mail.163.com/js6/read/readhtml.jsp?mid=' + e.emailId + '&sid='+sid
        # print url
        #
        # resp1 = requests.Session().post(url, data=data1, headers=headers)
        #
        # rs = resp1.content
        # print rs.decode('GBK')
        # print resp1.content

        #清空临时邮件表

        tempList = self.db_session.query(TempEmail).filter()
        for temp in tempList:
            self.db_session.delete(temp)

        #将邮件放入临时邮件表
        yhList = []
        for e in list:
            if '玉环农商行2018' in e.emailName:
                tempE = TempEmail(e.emailId)
                tempE.emailName = e.emailName
                yhList.append(e)
                self.db_session.add(tempE)
                self.db_session.commit()
        sql = 'select A.emailId from temp_email A where A.emailId not in  (select emailId from origin_email)'
        c = self.db_session.execute(sql)
        idList = []
        for row in c :
            print row[0]
            idList.append(row[0])

        newList = []
        for e in yhList:
            for eid in idList:
                if e.emailId == eid:
                    e.status = '0'
                    self.db_session.add(e)
                    newList.append(e)
                    self.db_session.commit()
                    self.parsePerEmail(e)

        return resp

    def __init__(self, u, p):
        self.password = p
        self.u = u
        self.db_session = ConnectDb().db_session

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

    # try:
    e = Email('15258297577@163.com', 'martha3137')
    resp = e.login()
    # except:
    #     print 'login err'

