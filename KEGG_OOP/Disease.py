from urllib.request import urlopen
from urllib.request import HTTPError
import urllib.request
import requests
import socket
from collections import OrderedDict

class Disease:
    
    def get_Disease_Name_Info_opt(self):

        DISEASE_URL = "http://rest.kegg.jp/list/disease"

        Name_Info_opt_List = []

        try:
            Disease_Info = urlopen(DISEASE_URL, None, timeout=1000000)

            while True:
                Disease_line = Disease_Info.readline()
                if not Disease_line: break
                Disease_new_line = str(Disease_line).split("\\t")

                Name_Info_opt_List.append(str(Disease_new_line[1]).replace("\\n'","").replace('"','').strip())

                #print(str(Disease_new_line[1]).replace("\\n'",""))

        except HTTPError as e:
            print(e)
        except TimeoutError as e:
            print(e)
        except socket.timeout:
            print('timeout')
        except Exception as e:
            print(e)

        return Name_Info_opt_List


    # KO와 연관된 Disease list 가져옴
    def get_KO_DISEASE_Link(self, KO):

        KO_DISEASE_List = []
        KO_DISEASE_URL = "http://rest.kegg.jp/link/disease/" + KO

        try:
            KO_DISEASE_Link = urlopen(KO_DISEASE_URL, None, timeout=100000)

            while True:
                KO_DISEASE_line = KO_DISEASE_Link.readline()
                if not KO_DISEASE_line: break

                Temp_KO_DISEASE_line = str(KO_DISEASE_line).split("\\tds:")

                KO_DISEASE_List.append(Temp_KO_DISEASE_line[1].replace("\\n'", ""))

            KO_DISEASE_List = list(OrderedDict.fromkeys(KO_DISEASE_List))

        except HTTPError as e:
            print("HTTPError")
            print(e)

        except TimeoutError as e:
            print("Timeout Error")
            print(e)

        except socket.timeout:
            print("Timeout")

        except Exception as e:
            print(e)

        return KO_DISEASE_List


    #Disease code로부터 포함된 모든 정보 추출
    def get_Disease_All_Info(self, Disease_code):

        DISEASE_INFO_URL = "http://rest.kegg.jp/get/" + Disease_code

        All_Info_List = []

        try:
            DISEASE_Info = urlopen(DISEASE_INFO_URL, None, timeout = 100000)


            while True:
                DISEASE_line = DISEASE_Info.readline()
                if not DISEASE_line: break

                All_Info_List.append(DISEASE_line)

                print(DISEASE_line)

        except HTTPError as e:
            print("HTTPError")
            print(e)

        except TimeoutError as e:
            print("Timeout Error")
            print(e)

        except socket.timeout:
            print("Timeout")

        except Exception as e:
            print(e)

        return All_Info_List

    #Disease code로부터 관련 Name 정보 추출
    def get_Disease_Name_Info(self, Disease_code):

        DISEASE_INFO_URL = "http://rest.kegg.jp/get/" + Disease_code

        Temp_List = []
        Name_Info_List = []

        try:
            DISEASE_Info = urlopen(DISEASE_INFO_URL, None, timeout = 100000)

            while True:
                DISEASE_line = DISEASE_Info.readline()
                if not DISEASE_line: break

                Temp_List.append(DISEASE_line)

            for ai in Temp_List:
                if str(ai).__contains__("NAME"):
                    #print(str(ai).replace("b'NAME        ","").replace('\\n',"").replace("'",""))
                    Name_Info_List.append(str(ai).replace("b'NAME        ","").replace('\\n',"").replace("'",""))

        except HTTPError as e:
            print("HTTPError")
            print(e)

        except TimeoutError as e:
            print("Timeout Error")
            print(e)

        except socket.timeout:
            print("Timeout")

        except Exception as e:
            print(e)

        return Name_Info_List

    #Disease code로부터 관련 Disease Description 정보 추출
    def get_Disease_Description_Info(self, Disease_code):

        DISEASE_INFO_URL = "http://rest.kegg.jp/get/" + Disease_code

        LineMarker = False
        Description_Info_List = []

        try:
            DISEASE_Info = urlopen(DISEASE_INFO_URL, None, timeout = 100000)

            while True:
                DISEASE_line = DISEASE_Info.readline()
                if not DISEASE_line: break

                if str(DISEASE_line).__contains__("b'DESCRIPTION "):
                    LineMarker = True
                    #print("LineMarker is true")

                elif str(DISEASE_line).__contains__("b'CATEGORY    "):
                    LineMarker = False
                    #print("LineMarker is false")

                if LineMarker == True:
                    #print(EC_line)
                    Description_Info_List.append(str(DISEASE_line).replace("b'DESCRIPTION ","").replace("b'            ","").replace('\\n',"").replace("'","").replace(";",""))

        except HTTPError as e:
            print("HTTPError")
            print(e)

        except TimeoutError as e:
            print("Timeout Error")
            print(e)

        except socket.timeout:
            print("Timeout")

        except Exception as e:
            print(e)

        return Description_Info_List


    #Disease code로부터 관련 category 정보 추출
    def get_Disease_Category_Info(self, Disease_code):

        DISEASE_INFO_URL = "http://rest.kegg.jp/get/" + Disease_code

        Temp_List = []
        Category_Info_List = []

        try:
            DISEASE_Info = urlopen(DISEASE_INFO_URL, None, timeout = 100000)

            while True:
                DISEASE_line = DISEASE_Info.readline()
                if not DISEASE_line: break

                Temp_List.append(DISEASE_line)

            for ai in Temp_List:
                if str(ai).__contains__("CATEGORY    "):
                    #print(str(ai).replace("b'CATEGORY    ","").replace('\\n',"").replace("'",""))
                    Category_Info_List.append(str(ai).replace("b'CATEGORY    ","").replace('\\n',"").replace("'",""))

        except HTTPError as e:
            print("HTTPError")
            print(e)

        except TimeoutError as e:
            print("Timeout Error")
            print(e)

        except socket.timeout:
            print("Timeout")

        except Exception as e:
            print(e)

        return Category_Info_List

    #Disease code로부터 관련 MeSH id 정보 추출

    def get_Disease_MeSH_id_Info(self, Disease_code):
        DISEASE_INFO_URL = "http://rest.kegg.jp/get/" + Disease_code

        Temp_List = []
        MeSH_id_Info_List = []

        try:
            # HTTP Error 403: Forbidden 에러 해결법 (봇 형태의 접근을 막는 에러)
            # 아래와 같이 코드를 작성하고 headers를 추가하면 됨

            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                       'Accept-Encoding': 'none',
                       'Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}

            req = urllib.request.Request(DISEASE_INFO_URL, headers = headers)
            response = urllib.request.urlopen(req).readlines()

            for info in response:

                if str(info).__contains__("b'            MeSH: "):
                    #print(str(info).replace("b'            ", "").replace('\\n', "").replace("'", "").replace("MeSH: ",""))
                    MeSH_id_Info_List.append(str(info).replace("b'            ","").replace('\\n',"").replace("'","").replace("MeSH: ",""))


        except HTTPError as e:
            print("HTTPError")
            print(e)

        except TimeoutError as e:
            print("Timeout Error")
            print(e)

        except socket.timeout:
            print("Timeout")

        except Exception as e:
            print(e)

        return MeSH_id_Info_List

    #Disease code로부터 관련 pathway 정보 추출
    def get_Disease_Pathway_Info(self, Disease_code):

        DISEASE_INFO_URL = "http://rest.kegg.jp/get/" + Disease_code

        Temp_List = []
        Pathway_Info_List = []

        try:
            DISEASE_Info = urlopen(DISEASE_INFO_URL, None, timeout = 100000)

            while True:
                DISEASE_line = DISEASE_Info.readline()
                if not DISEASE_line: break

                Temp_List.append(DISEASE_line)

            for ai in Temp_List:
                if str(ai).__contains__("     h"):
                    #print(ai)
                    #print(str(ai).replace("b'PATHWAY     ","").replace("b'            ","").replace('\\n',"").replace("'",""))
                    Pathway_Info_List.append(str(ai).replace("b'PATHWAY     ","").replace("b'            ","").replace('\\n',"").replace("'",""))

        except HTTPError as e:
            print("HTTPError")
            print(e)

        except TimeoutError as e:
            print("Timeout Error")
            print(e)

        except socket.timeout:
            print("Timeout")

        except Exception as e:
            print(e)

        return Pathway_Info_List
