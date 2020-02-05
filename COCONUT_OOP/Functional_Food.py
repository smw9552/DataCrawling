from urllib.request import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import socket


class Functional_Food:

    #COCONUT DB 내의 Function food ID로 접근하여 Name 정보 추출
    def get_Functional_Food_Name(self, ID):

        Functional_Food_Name_List = []

        try:
            html = urlopen("http://biosoft.kaist.ac.kr/coconut/db_food_result.jsp?ID="+ID)
            bsObject = BeautifulSoup(html, "html.parser")
            #웹 페이지의 정보를 txt로 만든 다음에 All_Text로 저장
            All_Text = bsObject.text

            #All_Text 정보를 줄바꿈으로 split하여 list 형태로 변환하여 저장
            TempList = All_Text.split("\n")

            #Name 이름 다음에 나오는 정보를 추가로 정리
            Functional_Food_Name_List.append(str(TempList[TempList.index("   Name  ")+1]).strip())

            #print(Functional_Food_Name_List)

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

        return Functional_Food_Name_List

    # COCONUT DB 내의 Function food ID로 접근하여 Function 정보 추출
    def get_Functional_Food_Function(self, ID):

        Functional_Food_Function_List = []

        try:
            html = urlopen("http://biosoft.kaist.ac.kr/coconut/db_food_result.jsp?ID="+ID)
            bsObject = BeautifulSoup(html, "html.parser")
            #웹 페이지의 정보를 txt로 만든 다음에 All_Text로 저장
            All_Text = bsObject.text

            # All_Text 정보를 줄바꿈으로 split하여 list 형태로 변환하여 저장
            TempList = All_Text.split("\n")

            # Name 이름 다음에 나오는 정보를 추가로 정리
            Functional_Food_Function_List.append(str(TempList[TempList.index("   Function  ") + 1]).strip())

            #print(Functional_Food_Function_List)

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

        return Functional_Food_Function_List

    # COCONUT DB 내의 Function food ID로 접근하여 Toxicity 정보 추출
    def get_Functional_Food_Toxicity(self, ID):

        Functional_Food_Toxicity_List = []

        try:
            html = urlopen("http://biosoft.kaist.ac.kr/coconut/db_food_result.jsp?ID="+ID)
            bsObject = BeautifulSoup(html, "html.parser")
            #웹 페이지의 정보를 txt로 만든 다음에 All_Text로 저장
            All_Text = bsObject.text

            # All_Text 정보를 줄바꿈으로 split하여 list 형태로 변환하여 저장
            TempList = All_Text.split("\n")

            #  이름 다음에 나오는 정보를 추가로 정리
            Functional_Food_Toxicity_List.append(str(TempList[TempList.index("   Toxicity  ") + 1]).strip())

            #print(Functional_Food_Toxicity_List)

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

        return Functional_Food_Toxicity_List
