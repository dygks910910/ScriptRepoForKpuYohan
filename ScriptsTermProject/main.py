
from DaumOpenApi import *
import testEmail
import os
def main():
    openAPI = DaumOpenAPI()
    cEmail = testEmail.EmailSystem()
    handler = testEmail.MyHandler
    while(True):
        print('=======================================================================================')
        print('한국 산업기술대학교 에서 가장 가까운 장소를 키워드로 검색하여 찾아주는 프로그램입니다.')
        print('게임공학과\n12학번\n박요한')
        print('=======================================================================================')

        print("1.검색\n2.검색결과 email로 보내기.\n3.웹서버에서 보기\n4.save to File.\n")
        menuNum = input("selletMenu(1~4):")
        if(menuNum == '1'):
            tempRss =  openAPI.getdataFromQuery(input('search:'))
            openAPI.printInfo(tempRss)
        elif(menuNum == '2'):
            cEmail.sendMailImportInfo(openAPI.getdataFromQuery(input('search keyword:')))
            pass
        elif(menuNum == '3'):
            handler.startWebService(handler)
            pass
        elif(menuNum == '4'):
            pass
        input("Press any key to continue. . .")
        os.system('cls')











if __name__ == "__main__":

    main()