
from module1 import *
from DaumOpenApi import *
import testEmail

def main():
    openAPI = DaumOpenAPI()
    cEmail = testEmail.EmailSystem()
    while(True):
        print('=======================================================================================')
        print('한국 산업기술대학교 에서 가장 가까운 장소를 키워드로 검색하여 찾아주는 프로그램입니다.')
        print('게임공학과\n12학번\n박요한')
        print('=======================================================================================')

        print("1.Search\n2.검색결과 email로 보내기.\n3.Search and send email\n4.save to File.\n")
        menuNum = input("selletMenu(1~4):")
        if(menuNum == '1'):
            tempRss =  openAPI.getdataFromQuery(input('검색어:'))
            openAPI.printInfo(tempRss)
        elif(menuNum == '2'):
            cEmail.sendMailImportInfo(openAPI.getdataFromQuery(input('검색어:')))
            pass
        elif(menuNum == '3'):
            pass
        elif(menuNum == '4'):
            pass











if __name__ == "__main__":

    main()