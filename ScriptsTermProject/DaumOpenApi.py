#-*- coding: utf-8 -*-
import urllib.request,urllib.parse 
from urllib.request import urlopen
import http.client
from urllib.parse import urlencode
from urllib.parse import quote_plus
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
    def __init__(self):
        print('init')
    def myURIBuilder(self,sellection = 1):
        if(sellection == 1):
            if(sellection == 1):
                self.queryParams = '?' + urlencode({ quote_plus('query') :self.query,
                               quote_plus('location') : self.location,
                               quote_plus('radius') : self.radius,
                               quote_plus('count') : self.count,
                               quote_plus('sort') : self.sort,
                               quote_plus('page') : self.page, 
                               quote_plus('apikey'):self.regKey
                                })
        elif(sellection == 2):
            if(sellection == 1):
                self.queryParams = '?' + urlencode({ quote_plus('query') : '센타',
                               quote_plus('location') : self.location,
                               quote_plus('radius') : self.radius,
                               quote_plus('count') : self.count,
                               quote_plus('sort') : self.sort,
                               quote_plus('page') : self.page, 
                               quote_plus('apikey'):self.regKey
                                })
    def getData(self):
        conn = http.client.HTTPConnection(self.server)
        print('connection complate')

        conn.request('GET',self.baseUrl+ self.queryParams )

        print('request complate\n')

        req = conn.getresponse()
        xmlData = req.read()
        print(req.status,req.reason)

        print(xmlData.decode('utf8'))
        pass


if __name__ == '__main__':
    a = DaumOpenAPI()
    print(a.myURIBuilder())
    #print(type(a.count))
    a.getData()