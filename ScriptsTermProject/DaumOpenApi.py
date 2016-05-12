
# -*- conding: utf-8 -*-

class DaumOpenAPI:
    #url�Է½� �� ���ĵ� 
    server = 'apis.daum.net/local/v1'
    regKey = '2839a18e2245d2a192247dd7d765e4c7'
    url = 'https://apis.daum.net/local/v1/search/keyword.xml?apikey=2839a18e2245d2a192247dd7d765e4c7' #url + apiKey
    query = 'temp'                          #�˻��� ���ϴ� ���Ǿ�.
    location = '37.340226,126.733629'               #����,�浵
    radius= '5000'                         #�߽���ǥ������ �ݰ�Ÿ�meter���� 0~20000
    count = '15'                          #�������� �Ǽ� 1~15
    page = '1'                            #������ ��ȣ1~3
    sort = '2'                            #0:��Ȯ���� , 1:�α�� , 2:�Ÿ���
    format = "xml"                        #�������� ���̽� Ȥ�� xml
    andSign = '&'
    conn = None
    def __init__():
        pass
    def userURIBuilder(self = self):
        url = {"http://" + self.server + "/search"+"/keyword."+self.format+"?"+"apikey="+self.regKey+self.andSign+
               "query="+self.query+self.andSign+"location="+self.location+self.andSign+
               'radius='+self.radius+self.andSign+'count='+self.count+self.andSign+'page='+self.andSign+
               'sort='+self.sort}

        return url




if __name__ == '__main__':
    a = DaumOpenAPI
    print(a.userURIBuilder(a))