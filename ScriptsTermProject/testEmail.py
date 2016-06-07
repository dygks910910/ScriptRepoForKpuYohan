

import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart #MIMEMultipart MIME 생성

#global value
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

     for bookitem in rss.findall('item'):#------------------------------------------------test
         # Bold 엘리먼트 생성
         b=newdoc.createElement('b')
         # 텍스트 노드 생성
         titletext=newdoc.createTextNode("장소명:"+bookitem.findtext('title'))
         b.appendChild(titletext)
         #print(titletext)

         body.appendChild(b)
         # <br> 부분 생성
         br = newdoc.createElement('br')
         body.appendChild(br)
         
         # title 부분 생성
         b = newdoc.createElement('p')
         # 텍스트 노드를 만듭니다.
         phonetext=newdoc.createTextNode('전화번호:'+bookitem.findtext('phone'))
         b.appendChild(phonetext)
        # print(phonetext)

         body.appendChild(b)
         body.appendChild(br)

          # 주소 부분 생성
         b = newdoc.createElement('p')
         # 텍스트 노드를 만듭니다.
         phonetext=newdoc.createTextNode('주소:'+bookitem.findtext('address'))
         b.appendChild(phonetext)
        # print(phonetext)

         body.appendChild(b)
         body.appendChild(br)

          # 도로명주소 부분 생성
         b = newdoc.createElement('p')
         # 텍스트 노드를 만듭니다.
         phonetext=newdoc.createTextNode('도로명주소:'+bookitem.findtext('newAddress'))
         b.appendChild(phonetext)
         #print(phonetext)

         body.appendChild(b)
         body.appendChild(br)

          # title 부분 생성
         b = newdoc.createElement('p')
         # 텍스트 노드를 만듭니다.
         phonetext=newdoc.createTextNode('거리:'+bookitem.findtext('distance'))
         b.appendChild(phonetext)
        # print(phonetext)

         body.appendChild(b)
         body.appendChild(br)
     # Body 엘리먼트를 취상위 엘리먼트에 추가

     top_element.appendChild(body)
     return newdoc.toxml()
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
#    def sendMail(self):
#     self.htmlFD = open(self.htmlFileName, 'rb')
#     self.HtmlPart = MIMEText(self.htmlFD.read(),'html', _charset = 'UTF-8' )
#     self.htmlFD.close()

## 만들었던 mime을 MIMEBase에 첨부 시킨다.
#     self.msg.attach(self.HtmlPart)

## 메일을 발송한다.
#     s = smtplib.SMTP(self.host,self.port)

##s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
#     s.ehlo()
#     s.starttls()
#     s.ehlo()
#     s.login(self.senderAddr,self.pw)
#     s.sendmail(self.senderAddr , [self.recipientAddr], self.msg.as_string())
#     s.close()


    def sendMailImportInfo(self,rss):

        title = str(input ('email Title :'))
        self.senderAddr = str(input ('sender email address :'))
        self.recipientAddr = str(input ('recipient email address :'))
        msgtext = str(input ('write message :'))
        self.pw= str(input (' input your password of email account :'))
        sellectImportData = str(input ('Do you want to include location data? (y/n):'))
        if sellectImportData == 'y' :
            html = self.MakeHtmlDoc(rss)
        
        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = title         #set message
        self.msg['From'] = self.senderAddr
        self.msg['To'] = self.recipientAddr    
        msgPart = MIMEText(msgtext, 'plain')
        bookPart = MIMEText(html, 'html', _charset = 'UTF-8') 
        self.msg.attach(msgPart) # 메세지에 생성한 MIME 문서를 첨부합니다
        self.msg.attach(bookPart)  
        print ("connect smtp server ... ")
        s = smtplib.SMTP(self.host,self.port) #python3.5에서는 smtplib.SMTP(host,port)

    #s.set_debuglevel(1)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(self.senderAddr, self.pw)    # 로그인  
        s.sendmail(self.senderAddr , [self.recipientAddr], self.msg.as_string())
        s.close()    
        print ("Mail sending complete!!!")
    
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

     for bookitem in rss.findall('item'):#------------------------------------------------test
         # Bold 엘리먼트 생성
         b=newdoc.createElement('b')
         # 텍스트 노드 생성
         titletext=newdoc.createTextNode("장소명:"+bookitem.findtext('title'))
         b.appendChild(titletext)
         #print(titletext)

         body.appendChild(b)
         # <br> 부분 생성
         br = newdoc.createElement('br')
         body.appendChild(br)
         
         # title 부분 생성
         b = newdoc.createElement('p')
         # 텍스트 노드를 만듭니다.
         phonetext=newdoc.createTextNode('전화번호:'+bookitem.findtext('phone'))
         b.appendChild(phonetext)
         #print(phonetext)

         body.appendChild(b)
         body.appendChild(br)

          # 주소 부분 생성
         b = newdoc.createElement('p')
         # 텍스트 노드를 만듭니다.
         phonetext=newdoc.createTextNode('주소:'+bookitem.findtext('address'))
         b.appendChild(phonetext)
         #print(phonetext)

         body.appendChild(b)
         body.appendChild(br)

          # 도로명주소 부분 생성
         b = newdoc.createElement('p')
         # 텍스트 노드를 만듭니다.
         phonetext=newdoc.createTextNode('도로명주소:'+bookitem.findtext('newAddress'))
         b.appendChild(phonetext)
         #print(phonetext)

         body.appendChild(b)
         body.appendChild(br)

          # title 부분 생성
         b = newdoc.createElement('p')
         # 텍스트 노드를 만듭니다.
         phonetext=newdoc.createTextNode('거리:'+bookitem.findtext('distance'))
         b.appendChild(phonetext)
         #print(phonetext)

         body.appendChild(b)
         body.appendChild(br)
     # Body 엘리먼트를 취상위 엘리먼트에 추가

     top_element.appendChild(body)
     return newdoc.toxml()
    
    


#if __name__ == '__main__':
#    import DaumOpenApi

#    api = DaumOpenApi.DaumOpenAPI()

#    s = EmailSystem()
#    s.sendMailImportInfo(api.getdataFromQuery('칼국수'))



#from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib.parse import urlparse
class MyHandler(BaseHTTPRequestHandler):
    from DaumOpenApi import DaumOpenAPI
    import sys
    serachKey = None
    a = DaumOpenAPI()
    def do_GET(self):
        #url 파싱해서 ‘=‘을 기준으로 keyword와 value로 문자열 구분
        url = self.a.getUrl(self.serachKey)
        #print(url)
        parts = urlparse(url)
        keyword, value = parts.query.split('=',1)#--------------------------------에러....

        #if keyword == 'count' : #keyword가 “title”인 경우
        #try:
        html = MakeHtmlDoc(self.a,(self.a.getdataFromQuery(self.serachKey))) #value제목검색 후 HTML전환
            ##헤더 부분 작성.
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html;charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8')) #  본분( body ) 부분 출력
        #else:
        #    self.send_error(400,' bad requst : please check the your url') # 잘못된 요청 응답

    def startWebService(self):
        self.serachKey = input('search Key:')
        try:
            server = HTTPServer( ('localhost',8080), MyHandler)
            print("started http server....")
            print('address = http://localhost:8080')
            server.serve_forever()
        except KeyboardInterrupt:
            print ("shutdown web server")
            server.socket.close()  # server 종료합니다.


 


if __name__ == '__main__':
    handler = MyHandler
    handler.startWebService(handler)
