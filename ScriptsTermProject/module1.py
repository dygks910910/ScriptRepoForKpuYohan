from urllib import *
from urllib.request import *
from urllib.parse import urlencode
from urllib.parse import quote_plus


# -*- conding: utf-8 -*-

def Parsing():
    key = " f%2BhwmVnBmOJ%2BRFy6p2FocJPRl32YalBVMXmrRhOJxAEk3OYfPiCVo7J%2FqlvN%2FFHm7JzgAQLePoBagzNaVLTQVQ%3D%3D "
    url = 'http://apis.data.go.kr/B551979/marineOrganismInhabitInfoService/getHabitatGisList'
    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : key, quote_plus('_type') : 'xml', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('staNum') : 'BA-Q-1', quote_plus('moNum') : '14', quote_plus('type') : '', quote_plus('searchKey') : '' })

    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    print(response_body)
    xmlFile = "test.xml"
    f = open(xmlFile,"w")
    f.write(response_body.decode())
    print("save complate")

#    key = "1GU47mzpc%2BRmSQ2u9URe0Z5kgAv6%2B42RG9evy6W5fMLgIaxg1r9qJOqnwNoAiwRh80I9X4EiWiyGex5oG1DnFQ%3D%3D"
#    url = """http://apis.data.go.kr/B551979/marineOrganismInhabitInfoService/getPhotographDescriptionHabitatList?type=1&searchKey=%EA%B0%AF%EA%B7%B8%EB%A0%B9&pageNo=1&numOfRows=10&_type=xml&ServiceKey="""
#    data = urllib.request.urlopen(url+key).read()
#    xmlFile = "test.xml"
#    print(data.decode('utf-8'))


if __name__ == '__main__':
    print('this is local')
    Parsing();
    
