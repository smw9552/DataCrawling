from urllib.request import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import socket

class Phenotype:

    #COCONUT DB 내의 Phenotype ID로 접근하여 Name 정보 추출
    def get_Phenotype_Name(self, ID):

        Phenotype_Name_List = []

        try:
            html = urlopen("http://biosoft.kaist.ac.kr/coconut/db_phen_result.jsp?ID="+ID)
            bsObject = BeautifulSoup(html, "html.parser")

            # 웹 페이지의 정보를 txt로 만든 다음에 All_Text로 저장
            All_Text = bsObject.text

            # All_Text 정보를 줄바꿈으로 split 하여 list 형태로 변환하여 저장
            TempList = All_Text.split("\n")

            #Name 다음에 나오는 정보를 추가로 정리
            Phenotype_Name_List.append(str(TempList[TempList.index("   Name  ")+1]).strip())

            #print(Phenotype_Name_List)


        except HTTPError as e:
            print("HTTPError")
            print(e)

        except TimeoutError as e:
            print("TimeoutError")
            print(e)

        except socket.timeout:
            print("Timeout")

        except Exception as e:
            print(e)

        return Phenotype_Name_List

    #COCONUT DB 내의 Phenotype ID로 접근하여 Semantic_type 정보 추출
    def get_Phenotype_Semantic_type(self, ID):

        Phenotype_Semantic_type_List = []

        try:
            html = urlopen("http://biosoft.kaist.ac.kr/coconut/db_phen_result.jsp?ID="+ID)
            bsObject = BeautifulSoup(html, "html.parser")

            # 웹 페이지의 정보를 txt로 만든 다음에 All_Text로 저장
            All_Text = bsObject.text

            # All_Text 정보를 줄바꿈으로 split 하여 list 형태로 변환하여 저장
            TempList = All_Text.split("\n")

            #Name 다음에 나오는 정보를 추가로 정리
            Phenotype_Semantic_type_List.append(str(TempList[TempList.index("   Semantic type  ")+1]).strip())

           # print(Phenotype_Semantic_type_List)


        except HTTPError as e:
            print("HTTPError")
            print(e)

        except TimeoutError as e:
            print("TimeoutError")
            print(e)

        except socket.timeout:
            print("Timeout")

        except Exception as e:
            print(e)

        return Phenotype_Semantic_type_List
