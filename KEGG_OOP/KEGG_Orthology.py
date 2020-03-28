from urllib.request import urlopen
from urllib.error import HTTPError
import socket

class KEGG_Orthology:

    def get_KO_Definition_Info_opt(self):

        KO_INFO_URL = "http://rest.kegg.jp/list/ko"

        Definition_Info_opt_List = []

        try:
            KO_Info = urlopen(KO_INFO_URL, None, timeout=1000000)

            while True:
                KO_line = KO_Info.readline()
                if not KO_line: break
                KO_new_line = str(KO_line).split("\\t")

                Definition_Info_opt_List.append(str(KO_new_line[1]).replace("\\n'","").replace('"','').strip())

                #print(str(KO_new_line[1]).replace("\\n'","").replace('"','').strip())

        except HTTPError as e:
            print(e)
        except TimeoutError as e:
            print(e)
        except socket.timeout:
            print('timeout')
        except Exception as e:
            print(e)

        return Definition_Info_opt_List



    #KO(KEGG Orthology)에 포함된 모든 정보 가지고 옴
    def get_KO_All_Info(self, KO_code):

        KO_INFO_URL = "http://rest.kegg.jp/get/" + KO_code

        All_Info_List = []

        try:

            KO_Info = urlopen(KO_INFO_URL, None, timeout = 100000)

            while True:
                KO_line = KO_Info.readline()
                if not KO_line: break

                All_Info_List.append(KO_line)


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

    #KO로부터 Name 정보 가지고 옴
    def get_KO_Name_Info(self, KO_code):

        KO_INFO_URL = "http://rest.kegg.jp/get/" + KO_code

        Temp_List = []
        Name_Info_List = []

        try:
            KO_Info = urlopen(KO_INFO_URL, None, timeout=100000)

            while True:
                KO_line = KO_Info.readline()
                if not KO_line: break

                Temp_List.append(KO_line)

            for ai in Temp_List:
                if str(ai).__contains__("NAME"):
                    Name_Info_List.append(str(ai).replace("b'NAME        ", "").replace('\\n', "").replace("'", ""))

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

    #KO로부터 Definition 정보 가지고 옴
    def get_KO_Definition_Info(self, KO_code):

        KO_INFO_URL = "http://rest.kegg.jp/get/" + KO_code

        Temp_List = []
        Definition_Info_List = []

        try:
            KO_Info = urlopen(KO_INFO_URL, None, timeout=100000)

            while True:
                KO_line = KO_Info.readline()
                if not KO_line: break

                Temp_List.append(KO_line)

            for ai in Temp_List:
                if str(ai).__contains__("DEFINITION"):
                    Definition_Info_List.append(str(ai).replace("b'DEFINITION  ", "").replace('\\n', "").replace("'", ""))

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

        return Definition_Info_List

    #KO로부터 Pathway 정보 가지고 옴
    def get_KO_Pathway_Info(self, KO_code):

        KO_INFO_URL = "http://rest.kegg.jp/get/" + KO_code

        LineMarker = False
        Pathway_Info_List = []

        try:
            KO_Info = urlopen(KO_INFO_URL, None, timeout=100000)

            while True:
                KO_line = KO_Info.readline()
                if not KO_line: break

                if str(KO_line).__contains__("PATHWAY"):
                    LineMarker = True

                elif str(KO_line).__contains__("BRITE"):
                    LineMarker = False

                if LineMarker == True:
                    Pathway_Info_List.append(str(str(KO_line).replace("b'PATHWAY     ","").replace('\\n', "").replace("'", "").replace("b            ","")).strip())

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


    #KO로부터 Module 정보 가지고 옴
    def get_KO_Module_Info(self, KO_code):

        KO_INFO_URL = "http://rest.kegg.jp/get/" + KO_code

        LineMarker = False
        Module_Info_List = []

        try:
            KO_Info = urlopen(KO_INFO_URL, None, timeout=100000)

            while True:
                KO_line = KO_Info.readline()
                if not KO_line: break

                if str(KO_line).__contains__("MODULE"):
                    LineMarker = True

                elif str(KO_line).__contains__("BRITE"):
                    LineMarker = False

                if LineMarker == True:
                    Module_Info_List.append(str(str(KO_line).replace("b'MODULE     ","").replace('\\n', "").replace("'", "").replace("b            ","")).strip())

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
