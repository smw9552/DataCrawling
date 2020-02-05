from urllib.request import urlopen
from urllib.request import HTTPError
import socket
from collections import OrderedDict

class Pathway:

    def get_Pathway_Name_Info_opt(self):

        PATHWAY_URL = "http://rest.kegg.jp/list/pathway"

        Name_Info_opt_List = []

        try:
            Pathway_Info = urlopen(PATHWAY_URL, None, timeout=1000000)

            while True:
                Pathway_line = Pathway_Info.readline()
                if not Pathway_line: break
                Pathway_new_line = str(Pathway_line).split("\\t")

                Name_Info_opt_List.append(str(Pathway_new_line[1]).replace("\\n'","").replace('"','').strip())

                #print(Pathway_new_line[1])

        except HTTPError as e:
            print(e)
        except TimeoutError as e:
            print(e)
        except socket.timeout:
            print('timeout')
        except Exception as e:
            print(e)

        return Name_Info_opt_List

    #KO와 연관된 Pathway list 가져옴
    def get_KO_PATHWAY_Link(self, KO):

        KO_PATHWAY_List = []
        KO_PATHWAY_URL = "http://rest.kegg.jp/link/pathway/" + KO

        try:
            KO_PATHWAY_Link = urlopen(KO_PATHWAY_URL, None, timeout=100000)

            while True:
                KO_PATHWAY_line = KO_PATHWAY_Link.readline()
                if not KO_PATHWAY_line: break

                Temp_KO_PATHWAY_line = str(KO_PATHWAY_line).split("\\tpath:")

                KO_PATHWAY_List.append(Temp_KO_PATHWAY_line[1].replace("\\n'","").replace("ko","map"))

            KO_PATHWAY_List = list(OrderedDict.fromkeys(KO_PATHWAY_List))

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

        return KO_PATHWAY_List

    #Pathway code로부터 포함된 모든 정보 가져옴
    def get_Pathway_All_Info(self, Pathway_code):

        PATHWAY_INFO_URL = "http://rest.kegg.jp/get/" + Pathway_code

        All_Info_List = []

        try:
            PATHWAY_Info = urlopen(PATHWAY_INFO_URL, None, timeout = 100000)


            while True:
                PATHWAY_line = PATHWAY_Info.readline()
                if not PATHWAY_line: break

                All_Info_List.append(PATHWAY_line)

                print(PATHWAY_line)

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

    #Pathway code로부터 관련 Name 정보 가져옴
    def get_Pathway_Name_Info(self, Pathway_code):

        PATHWAY_INFO_URL = "http://rest.kegg.jp/get/" + Pathway_code

        Temp_List = []
        Name_Info_List = []

        try:
            PATHWAY_Info = urlopen(PATHWAY_INFO_URL, None, timeout = 100000)

            while True:
                PATHWAY_line = PATHWAY_Info.readline()
                if not PATHWAY_line: break

                Temp_List.append(PATHWAY_line)

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

    #Pathway code로부터 관련 pathway class 정보 가져옴
    def get_Pathway_Class_Info(self, Pathway_code):

        PATHWAY_INFO_URL = "http://rest.kegg.jp/get/" + Pathway_code

        Temp_List = []
        Class_Info_List = []

        try:
            PATHWAY_Info = urlopen(PATHWAY_INFO_URL, None, timeout = 100000)

            while True:
                PATHWAY_line = PATHWAY_Info.readline()
                if not PATHWAY_line: break

                Temp_List.append(PATHWAY_line)

            for ai in Temp_List:
                if str(ai).__contains__("CLASS"):
                    #print(str(ai).replace("b'CLASS       ","").replace('\\n',"").replace("'",""))
                    Class_Info_List.append(str(ai).replace("b'CLASS       ","").replace('\\n',"").replace("'",""))

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

        return Class_Info_List

    #Pathway code로부터 관련 disease 정보 가져옴
    def get_Pathway_Disease_Info(self, Pathway_code):

        PATHWAY_INFO_URL = "http://rest.kegg.jp/get/" + Pathway_code

        Temp_List = []
        Disease_Info_List = []

        try:
            PATHWAY_Info = urlopen(PATHWAY_INFO_URL, None, timeout = 100000)

            while True:
                PATHWAY_line = PATHWAY_Info.readline()
                if not PATHWAY_line: break

                Temp_List.append(PATHWAY_line)

            for ai in Temp_List:
                if str(ai).__contains__("      H0"):
                    #print(ai)
                    #print(str(ai).replace("b'DISEASE     ","").replace("b'            ","").replace('\\n',"").replace("'",""))
                    Disease_Info_List.append(str(ai).replace("b'DISEASE     ","").replace("b'            ","").replace('\\n',"").replace("'",""))

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

        return Disease_Info_List

    #Pathway code로부터 관련 module 정보 가져옴
    def get_Pathway_Module_Info(self, Pathway_code):

        PATHWAY_INFO_URL = "http://rest.kegg.jp/get/" + Pathway_code

        Temp_List = []
        Module_Info_List = []

        try:
            PATHWAY_Info = urlopen(PATHWAY_INFO_URL, None, timeout = 100000)

            while True:
                PATHWAY_line = PATHWAY_Info.readline()
                if not PATHWAY_line: break

                Temp_List.append(PATHWAY_line)

            for ai in Temp_List:
                if str(ai).__contains__("      M0"):
                    #print(ai)
                    #print(str(ai).replace("b'MODULE      ","").replace("b'            ","").replace('\\n',"").replace("'",""))
                    Module_Info_List.append(str(ai).replace("b'MODULE      ","").replace("b'            ","").replace('\\n',"").replace("'",""))

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

        return Module_Info_List