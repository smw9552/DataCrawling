from urllib.request import urlopen
from urllib.error import HTTPError
import socket

class Metabolite:

    def get_Metabolite_Name_Info_opt(self):

        METABOLITE_URL = "http://rest.kegg.jp/list/cpd"

        Name_Info_opt_List = []

        try:
            Metabolite_Info = urlopen(METABOLITE_URL, None, timeout=1000000)

            while True:
                Metabolite_line = Metabolite_Info.readline()
                if not Metabolite_line: break
                Metabolite_new_Line = str(Metabolite_line).split("\\t")

                Name_Info_opt_List.append(str(Metabolite_new_Line[1]).replace("\\n'","").replace('"','').strip())

                #print(str(Metabolite_new_Line[1]).replace("\\n'","").strip())

        except HTTPError as e:
            print(e)
        except TimeoutError as e:
            print(e)
        except socket.timeout:
            print('timeout')
        except Exception as e:
            print(e)

        return Name_Info_opt_List

    #Metabolite에 대한 모든 정보 가지고 옴
    def get_Metabolite_All_Info(self, Metabolite_code):

        Metabolite_INFO_URL = "http://rest.kegg.jp/get/" + Metabolite_code

        All_Info_List = []

        try:
            Metabolite_Info = urlopen(Metabolite_INFO_URL, None, timeout=1000000)

            while True:
                Metabolite_line = Metabolite_Info.readline()
                if not Metabolite_line: break

                All_Info_List.append(Metabolite_line)

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

    #Metabolite에 대한 Name 정보 가지고 옴
    def get_Metabolite_Name_Info(self, Metabolite_code):

        Metabolite_INFO_URL = "http://rest.kegg.jp/get/" + Metabolite_code

        LineMarker = False
        Name_Info_List = []

        try:
            Metabolite_Info = urlopen(Metabolite_INFO_URL, None, timeout=1000000)

            while True:
                Metabolite_line = Metabolite_Info.readline()
                if not Metabolite_line: break

                if str(Metabolite_line).__contains__("NAME"):
                    LineMarker = True

                elif str(Metabolite_line).__contains__("FORMULA") or str(Metabolite_line).__contains__("COMMENT") or str(Metabolite_line).__contains__("REACTION") or \
                        str(Metabolite_line).__contains__("REMARK") or str(Metabolite_line).__contains__("BRITE") or str(Metabolite_line).__contains__("DBLINKS")\
                        or str(Metabolite_line).__contains__("PATHWAY") or str(Metabolite_line).__contains__("SEQUENCE"):
                    LineMarker = False

                if LineMarker == True:
                    Name_Info_List.append(str(str(Metabolite_line).replace("b'NAME      ", "").replace('b"NAME      ','')
                                              .replace('b"            ',"").replace('\\n', "").replace("'", "")
                                              .replace('"','').replace('b"','').replace("NAME        ","")
                                              .replace("b            ","")).strip())

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

    #Metabolite에 대한 Formula 정보 가지고 옴
    def get_Metabolite_Formula_Info(self, Metabolite_code):

        Metabolite_INFO_URL = "http://rest.kegg.jp/get/" + Metabolite_code

        LineMarker = False
        Formula_Info_List = []

        try:
            Metabolite_Info = urlopen(Metabolite_INFO_URL, None, timeout=1000000)

            while True:
                Metabolite_line = Metabolite_Info.readline()
                if not Metabolite_line: break

                if str(Metabolite_line).__contains__("FORMULA"):
                    LineMarker = True

                elif str(Metabolite_line).__contains__("EXACT_MASS") or str(Metabolite_line).__contains__("COMMENT")\
                        or str(Metabolite_line).__contains__("b'COMMENT     ") or str(Metabolite_line).__contains__('b"COMMENT     ')\
                        or str(Metabolite_line).__contains__("DBLINKS") or str(Metabolite_line).__contains__("REMARK")\
                        or str(Metabolite_line).__contains__("REACTION"):
                    LineMarker = False

                if LineMarker == True:
                    Formula_Info_List.append(str(str(Metabolite_line).replace("b'FORMULA     ", "").replace('b"            ',"").replace('\\n', "").replace("'", "").replace('"','').replace("b", "")).strip())

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

        return Formula_Info_List

    #Metabolite에 대한 Molecular_weight 정보 가지고 옴
    def get_Metabolite_Molecular_Weight_Info(self, Metabolite_code):

        Metabolite_INFO_URL = "http://rest.kegg.jp/get/" + Metabolite_code

        LineMarker = False
        Molecular_Weight_Info_List = []

        try:
            Metabolite_Info = urlopen(Metabolite_INFO_URL, None, timeout=1000000)

            while True:
                Metabolite_line = Metabolite_Info.readline()
                if not Metabolite_line: break

                #print(Metabolite_line)

                if str(Metabolite_line).__contains__("MOL_WEIGHT"):
                    LineMarker = True

                elif str(Metabolite_line).__contains__("REACTION") or str(Metabolite_line).__contains__("REMARK") \
                        or str(Metabolite_line).__contains__("COMMNET") or str(Metabolite_line).__contains__("DBLINKS") \
                        or str(Metabolite_line).__contains__("PATHWAY") or str(Metabolite_line).__contains__("BRITE") \
                        or str(Metabolite_line).__contains__("ENZYME") or str(Metabolite_line).__contains__("SEQUENCE")\
                        or str(Metabolite_line).__contains__("b'COMMENT     ") or str(Metabolite_line).__contains__('b"COMMENT     '):
                    LineMarker = False

                if LineMarker == True:

                    Molecular_Weight_Info_List.append(str(str(Metabolite_line).replace("b'MOL_WEIGHT  ", "").replace('b"            ',"").replace('\\n', "").replace("'", "").replace('"','').replace("b", "")).strip())

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

        return Molecular_Weight_Info_List

    #Metabolite에 대한 Reaction 정보 가지고 옴
    def get_Metabolite_Reaction_Info(self, Metabolite_code):

        Metabolite_INFO_URL = "http://rest.kegg.jp/get/" + Metabolite_code

        LineMarker = False
        Reaction_Info_List = []

        try:
            Metabolite_Info = urlopen(Metabolite_INFO_URL, None, timeout=1000000)

            while True:
                Metabolite_line = Metabolite_Info.readline()
                if not Metabolite_line: break

                if str(Metabolite_line).__contains__("REACTION"):
                    LineMarker = True

                elif str(Metabolite_line).__contains__("PATHWAY"):
                    LineMarker = False

                if LineMarker == True:

                    Reaction_Info_List.append(str(str(Metabolite_line).replace("b'REACTION  ", "").replace('b"            ',"").replace('\\n', "").replace("'", "").replace('"','').replace("b", "")).strip())

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

        return Reaction_Info_List

    #Metabolite에 대한 Pathway 정보 가지고 옴
    def get_Metabolite_Pathway_Info(self, Metabolite_code):

        Metabolite_INFO_URL = "http://rest.kegg.jp/get/" + Metabolite_code

        LineMarker = False
        Pathway_Info_List = []

        try:
            Metabolite_Info = urlopen(Metabolite_INFO_URL, None, timeout=1000000)

            while True:
                Metabolite_line = Metabolite_Info.readline()
                if not Metabolite_line: break

                if str(Metabolite_line).__contains__("PATHWAY"):
                    LineMarker = True

                elif str(Metabolite_line).__contains__("MODULE"):
                    LineMarker = False

                if LineMarker == True:

                    Pathway_Info_List.append(str(str(Metabolite_line).replace("b'PATHWAY  ", "").replace('b"            ',"").replace('\\n', "").replace("'", "").replace('"','').replace("b", "")).strip())

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

    #Metabolite에 대한 Enzyme 정보 가지고 옴
    def get_Metabolite_Enzyme_Info(self, Metabolite_code):

        Metabolite_INFO_URL = "http://rest.kegg.jp/get/" + Metabolite_code

        LineMarker = False
        Enzyme_Info_List = []

        try:
            Metabolite_Info = urlopen(Metabolite_INFO_URL, None, timeout=1000000)

            while True:
                Metabolite_line = Metabolite_Info.readline()
                if not Metabolite_line: break

                if str(Metabolite_line).__contains__("ENZYME"):
                    LineMarker = True

                elif str(Metabolite_line).__contains__("DBLINKS"):
                    LineMarker = False

                if LineMarker == True:

                    Enzyme_Info_List.append(str(str(Metabolite_line).replace("b'ENZYME  ", "").replace('b"            ',"").replace('\\n', "").replace("'", "").replace('"','').replace("b", "")).strip())

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

        return Enzyme_Info_List

