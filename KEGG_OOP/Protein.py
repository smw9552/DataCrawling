from urllib.request import urlopen
from urllib.error import HTTPError
import socket
from collections import OrderedDict

class Protein:

    def get_EC_Name_Info_opt(self):

        EC_URL = "http://rest.kegg.jp/list/ec"

        Name_Info_opt_List = []

        try:
            EC_info = urlopen(EC_URL, None, timeout=1000000)

            while True:
                EC_line = EC_info.readline()
                if not EC_line: break
                EC_new_line = str(EC_line).split("\\t")

                Name_Info_opt_List.append(str(EC_new_line[1]).replace("\\n'","").replace('"','').strip())
                #print(EC_new_line[1])

        except HTTPError as e:
            print(e)
        except TimeoutError as e:
            print(e)
        except socket.timeout:
            print('timeout')
        except Exception as e:
            print(e)

        return Name_Info_opt_List

    #KO와 연관된 EC list 가져옴
    def get_KO_EC_Link(self, KO):

        KO_EC_List = []
        KO_EC_URL = "http://rest.kegg.jp/link/ec/" + KO

        try:
            KO_EC_Link = urlopen(KO_EC_URL, None, timeout=100000)

            while True:
                KO_EC_line = KO_EC_Link.readline()
                if not KO_EC_line: break

                Temp_KO_EC_line = str(KO_EC_line).split("\\tec:")

                KO_EC_List.append(Temp_KO_EC_line[1].replace("\\n'",""))

            KO_EC_List = list(OrderedDict.fromkeys(KO_EC_List))

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

        return KO_EC_List

    #EC code로부터 포함된 모든 정보 가져옴
    def get_EC_All_Info(self, EC_code):

        EC_INFO_URL = "http://rest.kegg.jp/get/" + EC_code

        All_Info_List = []

        try:
            EC_Info = urlopen(EC_INFO_URL, None, timeout = 100000)


            while True:
                EC_line = EC_Info.readline()
                if not EC_line: break

                All_Info_List.append(EC_line)

                print(EC_line)

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

    #EC code로부터 관련 Name 정보 가져옴
    def get_EC_Name_Info(self, EC_code):

        EC_INFO_URL = "http://rest.kegg.jp/get/" + EC_code

        LineMarker = False
        Name_Info_List = []

        try:
            EC_Info = urlopen(EC_INFO_URL, None, timeout = 100000)

            while True:
                EC_line = EC_Info.readline()
                if not EC_line: break

                #print(EC_line)

                if str(EC_line).__contains__("b'NAME        ") \
                        or str(EC_line).__contains__('b"NAME        '):
                    LineMarker = True

                elif str(EC_line).__contains__("b'CLASS       ") or str(EC_line).__contains__('b"SYSNAME     '):
                    LineMarker = False

                if LineMarker == True:
                    Name_Info_List.append(str(EC_line).replace("NAME        ","")
                                          .replace("b'NAME        ","").replace("b'            ","")
                                          .replace('\\n',"").replace("'","")
                                          .replace(";","").replace("b","").replace('"            ',"")
                                          .replace('"','').strip())

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

    #EC code로부터 관련 Class 정보 가져옴
    def get_EC_Class_Info(self, EC_code):

        EC_INFO_URL = "http://rest.kegg.jp/get/" + EC_code

        LineMarker = False
        Class_Info_List = []

        try:
            EC_Info = urlopen(EC_INFO_URL, None, timeout = 100000)

            while True:
                EC_line = EC_Info.readline()
                if not EC_line: break

                #print(EC_line)

                if str(EC_line).__contains__("b'CLASS       "):
                    LineMarker = True
                    #print("LineMarker is true")

                elif str(EC_line).__contains__("b'SYSNAME     ") \
                        or str(EC_line).__contains__('b"SYSNAME     ')\
                        or str(EC_line).__contains__("b'COMMENT     ")\
                        or str(EC_line).__contains__('b"COMMENT     ')\
                        or str(EC_line).__contains__('b"REACTION    ')\
                        or str(EC_line).__contains__("b'REACTION    "):
                    LineMarker = False
                    #print("LineMarker is false")

                if LineMarker == True:
                    #print(EC_line)
                    Class_Info_List.append(str(EC_line).replace("b'CLASS       ","")
                                           .replace("b'            ","").replace('\\n',"")
                                           .replace("'","").replace(";","")
                                           .replace('b"            ','')
                                           .replace('"','').strip())

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

    #EC code로부터 관련 Reaction equation 정보 가져옴
    def get_EC_Reaction_eq_Info(self, EC_code):

        EC_INFO_URL = "http://rest.kegg.jp/get/" + EC_code

        LineMarker = False
        Reaction_eq_Info_List = []

        try:
            EC_Info = urlopen(EC_INFO_URL, None, timeout = 100000)

            while True:
                EC_line = EC_Info.readline()
                if not EC_line: break

                #print(EC_line)

                if str(EC_line).__contains__("b'REACTION    "):
                    LineMarker = True
                    #print("LineMarker is true")

                elif str(EC_line).__contains__("b'ALL_REAC    "):
                    LineMarker = False
                    #print("LineMarker is false")

                if LineMarker == True:
                    #print(EC_line)
                    Reaction_eq_Info_List.append(str(EC_line).replace("b'REACTION    ","")
                                                 .replace("b'            ","").replace('\\n',"")
                                                 .replace("'","").replace(";","").strip())

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

        return Reaction_eq_Info_List


    #EC code로부터 관련 Reaction code 정보 가져옴
    def get_EC_Reaction_code_Info(self, EC_code):

        EC_INFO_URL = "http://rest.kegg.jp/get/" + EC_code

        LineMarker = False
        Reaction_code_Info_List = []

        try:
            EC_Info = urlopen(EC_INFO_URL, None, timeout = 100000)

            while True:
                EC_line = EC_Info.readline()
                if not EC_line: break

                #print(EC_line)

                if str(EC_line).__contains__("b'ALL_REAC    "):
                    LineMarker = True
                    #print("LineMarker is true")

                elif str(EC_line).__contains__("b'SUBSTRATE   "):
                    LineMarker = False
                    #print("LineMarker is false")

                if LineMarker == True:
                    #print(EC_line)
                    Reaction_code_Info_List.append(str(EC_line).replace("b'ALL_REAC    ","")
                                                   .replace("b'            ","").replace('\\n',"")
                                                   .replace("'","").replace(";","").strip())

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

        return Reaction_code_Info_List


    #EC code로부터 관련 Reaction의 substrate 정보 가져옴
    def get_EC_Substrate_Info(self, EC_code):

        EC_INFO_URL = "http://rest.kegg.jp/get/" + EC_code

        LineMarker = False
        Substrate_Info_List = []

        try:
            EC_Info = urlopen(EC_INFO_URL, None, timeout = 100000)

            while True:
                EC_line = EC_Info.readline()
                if not EC_line: break

                #print(EC_line)

                if str(EC_line).__contains__("b'SUBSTRATE   "):
                    LineMarker = True
                    #print("LineMarker is true")

                elif str(EC_line).__contains__("b'PRODUCT     "):
                    LineMarker = False
                    #print("LineMarker is false")

                if LineMarker == True:
                    #print(EC_line)
                    Substrate_Info_List.append(str(EC_line).replace("b'SUBSTRATE   ","")
                                               .replace("b'            ","").replace('\\n',"")
                                               .replace("'","").replace(";","").strip())

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

        return Substrate_Info_List


    #EC code로부터 관련 Reaction의 product 정보 가져옴
    def get_EC_Product_Info(self, EC_code):

        EC_INFO_URL = "http://rest.kegg.jp/get/" + EC_code

        LineMarker = False
        Product_Info_List = []

        try:
            EC_Info = urlopen(EC_INFO_URL, None, timeout = 100000)

            while True:
                EC_line = EC_Info.readline()
                if not EC_line: break

                #print(EC_line)

                if str(EC_line).__contains__("b'PRODUCT     "):
                    LineMarker = True
                    #print("LineMarker is true")

                elif str(EC_line).__contains__("b'COMMENT     "):
                    LineMarker = False
                    #print("LineMarker is false")

                if LineMarker == True:
                    #print(EC_line)
                    Product_Info_List.append(str(EC_line).replace("b'PRODUCT     ","")
                                             .replace("b'            ","").replace('\\n',"")
                                             .replace("'","").replace(";","").strip())

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

        return Product_Info_List


    def get_EC_CPD_code_Info(self, EC_code):

        EC_INFO_URL = "http://rest.kegg.jp/get/" + EC_code

        LineMarker = False
        CPD_code_Info_List = []

        try:
            EC_Info = urlopen(EC_INFO_URL, None, timeout = 100000)

            while True:
                EC_line = EC_Info.readline()
                if not EC_line: break

                #print(EC_line)

                if str(EC_line).__contains__(" [CPD:"):
                    LineMarker = True
                    #print("LineMarker is true")

                elif str(EC_line).__contains__("b'COMMENT     "):
                    LineMarker = False
                    #print("LineMarker is false")

                if LineMarker == True:
                    #print(str(EC_line))
                    #print((str((str(EC_line).split(" [CPD:")[1])).replace("];", "")).replace("]","").replace("\\n'",""))

                    CPD_code_Info_List.append((str((str(EC_line).split(" [CPD:")[1])).replace("];", ""))
                                              .replace("]","").replace("\\n'","")
                                              .replace('"','').strip())

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

        return CPD_code_Info_List

