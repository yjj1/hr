# -*- coding:'utf8' -*-
#encoding=utf8

import json
import os
if __name__ == '__main__':
    data = {'code':'ok'}
    str = json.dumps(data)
    # s = '{"code":}'
    # s = '{"code":"S_OK","var":{"from":["Mango_Y <562550671@qq.com>"],"to":["15258297577 <15258297577@163.com>"],"flags":{},"requestReadReceipt":false,"isManualDisposition":true,"subject":"玉环农商行2018_叶坚静_计算机科学与技术_1991.10.15_男_15258297577_科技岗","sentDate":new Date(2017,11,4,15,13,44),"priority":3,"headerRaw":"Received: from smtpbg331.qq.com (unknown [14.17.43.223])\r\n\tby mx40 (Coremail) with SMTP id WsCowAAXDqup9SRaplxbCg--.20011S3;\r\n\tMon, 04 Dec 2017 15:13:45 +0800 (CST)\r\nDKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=qq.com; s=s201512;\r\n\tt=1512371625; bh=MOYMC9PuJQa6C9J+NfejDsvD6FB7GnzmuoJlc6fL3TM=;\r\n\th=From:To:Subject:Mime-Version:Content-Type:Content-Transfer-Encoding:Date:Message-ID;\r\n\tb=xUMjO+8J3o/xYTVjYlbHFO81cttqGeOhnpdXblXGZXtd27mPKXF2NLwwfrReOfpJ3\r\n\t EMEo2b4eBclroaBgZsa6si4UPusQFuYCNaMlIiz6pyI44urU7AGvWcjVIjf/9of6wC\r\n\t t+/bW5cfRlTwh28hFhj8Qx/tAP7m9POGlKB2NgZE=\r\nX-QQ-FEAT: 2PHmmy4qbuL/2ZHHzytQeYy7a0ONT9t2xcJmWCT3CACI+Xu2kQRMcXih0BFbF\r\n\tSBd83r3CNsQ37id2NY4CC6XoBp3gvB7CWCpOOkSIAEYZXNJyxuvDTYzEOvbrJGt30HoDJm9\r\n\tB1HxvxJVxkKkB3bhZzgprH/BVC3UuhV42ymdss0qFqth5rEl4Uzu4M1aR9qa08KN+rm6DZG\r\n\tkiSO2qunax99OF2beJR7mXkTEOLkAt6PXKKua3uqni7hr9bkS/B/vvsMnUa0ilD/MzuSGOG\r\n\t5KHA==\r\nX-QQ-SSF: 000000000000002000000000000000Z\r\nX-HAS-ATTACH: no\r\nX-QQ-BUSINESS-ORIGIN: 2\r\nX-Originating-IP: 122.226.109.182\r\nX-QQ-STYLE: \r\nX-QQ-mid: webmail79t1512371624t9172875\r\nFrom: "=?gb18030?B?TWFuZ29fWQ==?=" <562550671@qq.com>\r\nTo: "=?gb18030?B?MTUyNTgyOTc1Nzc=?=" <15258297577@163.com>\r\nSubject: =?gb18030?B?0/G7t8WpyczQ0DIwMThf0ra84b6yX7zGy+O7+r/G?=\r\n =?gb18030?B?0afT67y8yvVfMTk5MS4xMC4xNV/E0F8xNTI1ODI5?=\r\n =?gb18030?B?NzU3N1+/xry8uNo=?=\r\nMime-Version: 1.0\r\nContent-Type: multipart/mixed;\r\n\tboundary="----=_NextPart_5A24F5A8_09554270_1F8B7DF3"\r\nContent-Transfer-Encoding: 8Bit\r\nDate: Mon, 4 Dec 2017 15:13:44 +0800\r\nX-Priority: 3\r\nMessage-ID: <tencent_288966153588947BA06C9A778832BB70CA08@qq.com>\r\nX-QQ-MIME: TCMime 1.0 by Tencent\r\nX-Mailer: QQMail 2.x\r\nX-QQ-Mailer: QQMail 2.x\r\nX-QQ-SENDSIZE: 520\r\nReceived: from qq.com (unknown [127.0.0.1])\r\n\tby smtp.qq.com (ESMTP) with SMTP\r\n\tid ; Mon, 04 Dec 2017 15:13:44 +0800 (CST)\r\nFeedback-ID: webmail:qq.com:bgweb:bgweb133\r\nX-CM-TRANSID:WsCowAAXDqup9SRaplxbCg--.20011S3\r\nAuthentication-Results: mx40; spf=pass smtp.mail=562550671@qq.com; dki\r\n\tm=pass header.i=@qq.com\r\nX-Coremail-Antispam: 1Uf129KBjDUn29KB7ZKAUJ8b5iA529EdanIXcx71UUUUU7v73\r\n\tVFW2AGmfu7bjvjm3AaLaJ3UbIYCTnIWIevJa73UjIFyTuYvjxUsXo2DUUUU\r\n","headers":{},"antispamInfo":{"RulesType":"","GuestSender":null},"html":{"id":"2","contentType":"text/html","contentLength":22,"encoding":"base64","contentOffset":2591,"estimateSize":15},"text":{"id":"1","contentType":"text/plain","contentLength":2,"encoding":"base64","contentOffset":2459,"estimateSize":0},"attachments":[{"id":"3","filename":"玉环农商行2018_叶坚静_计算机科学与技术_1991.10.15_男_15258297577_科技岗.doc","contentType":"application/msword","contentLength":58938,"encoding":"base64","contentOffset":3092,"estimateSize":43071}]}}';
    # s = s.replace('\t','')
    # s = s.replace('\r','')
    # s = s.replace('\n','')
    s = '{"sentDate":"aaa"}'
    js = json.loads(s)
    print js['sentDate']

    str = 'xxdoc'

    v = os.path.splitext(str)
    print v[1]