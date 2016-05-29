#-*- coding: utf-8 -*-
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


    def __init__(self):
        print('init')
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

        print('request complate\n')

        req = conn.getresponse()
        self.xmlData = req.read()
        print(req.status,req.reason)

        print(self.xmlData.decode('utf8'))

    def updateQueryParam(self):
        tempInput = input('Search Key:')

        self.query = tempInput
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
        #tree = ElementTree.fromstring(self.xmlData)
        #print(self.xmlData)
        #itemElements = tree.getiterator('item')
        #print(itemElements)
        #rss = ElementTree.parse(urlopen(self.baseUrl + self.queryParams())).getroot()
       
        #for element in rss.findall('item'):
        #    print(element.findtext('title')
       rss = (ElementTree.parse(urlopen(self.baseUrl + self.queryParams))).getroot()

       self.printInfo(rss)
    def getdataFromQuery(self):
        self.updateQueryParam()
        rss = (ElementTree.parse(urlopen(self.baseUrl + self.queryParams))).getroot()
        return rss

if (__name__ == '__main__') :
    a = DaumOpenAPI()
    while(1):
        #print(type(a.count))
        a.printInfo(a.getdataFromQuery())
        #a.getData()
