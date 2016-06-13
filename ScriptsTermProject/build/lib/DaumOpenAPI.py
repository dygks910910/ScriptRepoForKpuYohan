# -*- coding: utf-8 -*-
import urllib.request,urllib.parse 
from urllib.request import urlopen
import http.client
from urllib.parse import urlencode
from urllib.parse import quote_plus
from xml.etree import ElementTree
class DaumOpenAPI:
    #url�Է½� �� ���ĵ� 
    server = 'apis.daum.net'
    nextServer = '/local/v1'
    regKey = '2839a18e2245d2a192247dd7d765e4c7'
    query = '스타벅스'                          #질의검색
    location = '37.340226,126.733629'               #위도경도
    radius= '20000'                         #반경 0~20000
    count = '15'                          #페이지에 보여질 갯수1~15
    page = '1'                            #페이지번호1~3
    sort = '2'                            #0:정확도, 1:거리, 2:인기
    format = "xml"                        #xml
    andSign = '&'
    conn = None
    queryParams =None
    baseUrl = 'http://apis.daum.net/local/v1/search/keyword.xml'
    xmlData = None


    #def __init__(self):
        #print('init')
    def myURIBuilder(self):
         self.queryParams = ('?' + urlencode({ quote_plus('query') : self.query,
                               quote_plus('location') : self.location,
                               quote_plus('radius') : self.radius,
                               quote_plus('count') : self.count,
                               quote_plus('sort') : self.sort,
                               quote_plus('page') : self.page, 
                               quote_plus('apikey'):self.regKey
                                }))
    #검색할 장소 xml형식으로 불러오기    

    def getData(self): 
        conn = http.client.HTTPConnection(self.server)
        print('connection complate')

        conn.request('GET',self.baseUrl+ self.queryParams )
        print(self.baseUrl+ self.queryParams)
        print('request complate\n')

        req = conn.getresponse()
        self.xmlData = req.read()
        print(req.status,req.reason)

        print(self.xmlData.decode('utf8'))

    def updateQueryParam(self,key):

        self.query = key
        self.myURIBuilder()

    def printInfo(self,rss):
        for element in rss.findall("item"):
           print('-------------------------------------------------------------------------------')

           print('장소명:'+element.findtext('title'))

           print('카테고리:'+element.findtext('category'))

           print('전화번호:'+element.findtext('phone'))

           print('구주소:'+element.findtext('address'))

           print('도로명주소:'+element.findtext('newAddress'))

           print('거리:'+element.findtext('distance')+'미터')

           print('방향:'+element.findtext('direction'))
           print('-------------------------------------------------------------------------------')
    def extractTitleData(self):
       rss = (ElementTree.parse(urlopen(self.baseUrl + self.queryParams))).getroot()
       
       self.printInfo(rss)
    def getdataFromQuery(self,key):
        self.updateQueryParam(key)
        rss = (ElementTree.parse(urlopen(self.baseUrl + self.queryParams))).getroot()
        return rss
    def getUrl(self,key):
        self.updateQueryParam(key)
        return self.baseUrl + self.queryParams
    def fileOut(self):
        myQuery = None
        f = open("자료.txt", 'w')
        
        rss =DaumOpenAPI.getdataFromQuery(self,input("search:"))
        for element in rss.findall("item"):

           place = '장소명:'+element.findtext('title')+'\n'

           category = '카테고리:'+element.findtext('category') + '\n'

           phone = '전화번호:'+element.findtext('phone')+'\n'

           address = '구주소:'+element.findtext('address')+'\n'

           newaddress = '도로명주소:'+element.findtext('newAddress')+'\n'

           distance = '거리:'+element.findtext('distance')+'미터'+'\n'

           direction = '방향:'+element.findtext('direction')+'\n'

           endline = '-------------------------------------------------------------------------------'+'\n'
           
           f.write(endline)
           f.write(place)
           f.write(category)
           f.write(phone)
           f.write(address)
           f.write(newaddress)
           f.write(distance)
           f.write(direction)
           f.write(endline)

        f.close()
        print("파일출력 완료")


if (__name__ == '__main__') :
    a = DaumOpenAPI()
    a.fileOut()