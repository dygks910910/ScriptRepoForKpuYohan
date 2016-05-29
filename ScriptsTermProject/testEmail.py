import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

#global value

class EmailSystem:
    host = "smtp.gmail.com" # Gmail STMP 서버 주소.
    port = "587"
    htmlFileName = "logo.html"
    senderAddr= None
    recipientAddr= None
    htmlFD = None
    HtmlPart = None
    pw = 'qkrdygks33'
    msg = None
    def __init__(self):
        self.senderAddr = "dygks910@gmail.com" # 보내는 사람 email 주소.
        self.recipientAddr = "dygks910910@daum.net"   	# 받는 사람 email 주소.
        self.msg = MIMEBase("multipart", "alternative")
        self.msg['Subject'] = "Test email in Python 3.5"
        self.msg['From'] = self.senderAddr
        self.msg['To'] = self.recipientAddr

# MIME 문서를 생성합니다.
    def sendMail(self):
     self.htmlFD = open(self.htmlFileName, 'rb')
     self.HtmlPart = MIMEText(self.htmlFD.read(),'html', _charset = 'UTF-8' )
     self.htmlFD.close()
# 만들었던 mime을 MIMEBase에 첨부 시킨다.
     self.msg.attach(self.HtmlPart)
# 메일을 발송한다.
     s = smtplib.SMTP(self.host,self.port)
#s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
     s.ehlo()
     s.starttls()
     s.ehlo()
     s.login(self.senderAddr,self.pw)
     s.sendmail(self.senderAddr , [self.recipientAddr], self.msg.as_string())
     s.close()
    def setInfoForInput(self,rss):
        title = str(input ('Title :'))
        self.senderAddr = str(input ('sender email address :'))
        self.recipientAddr = str(input ('recipient email address :'))
        msgtext = str(input ('write message :'))
        self.pw= str(input (' input your password of gmail account :'))
        sellectImportData = str(input ('Do you want to include location data? (y/n):'))
        if sellectImportData == 'y' :
            keyword = str(input ('input keyword to search:'))
            html = MakeHtmlDoc(rss)

        pass

    def MakeHtmlDoc(self,rss):
     from xml.dom.minidom import getDOMImplementation
     # DOM 개체를 생성
     impl = getDOMImplementation()

     newdoc=impl.createDocument(None, 'html', None)
     top_element = newdoc.documentElement
     header = newdoc.createElement('header')
     top_element.appendChild(header)
     #Body 엘리먼트를 생성
     body = newdoc.createElement('body')

     for bookitem in rss:#------------------------------------------------test
         # Bold 엘리먼트 생성
         b=newdoc.createElement('b')
         # 텍스트 노드 생성
         itemText=newdoc.createTextNode("item:")
         b.appendChild(itemText)
         body.appendChild(b)
         # <br> 부분 생성
         br = newdoc.createElement('br')
         body.appendChild(br)
         # title 부분 생성
         p = newdoc.createElement('p')
         # 텍스트 노드를 만듭니다.
         titleText=newdoc.createTextNode('Title:')
         p.appendChild(titleText)
         body.appendChild(p)
         body.appendChild(br)
     # Body 엘리먼트를 취상위 엘리먼트에 추가
     top_element.appendChild(body)
     return newdoc.toxml()

if __name__ == '__main__':
    s = EmailSystem()
    s.sendMail()
    pass