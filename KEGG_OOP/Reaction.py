from urllib.request import urlopen
from urllib.request import HTTPError
import socket

class Reaction:

    def get_Reaction_Name_Info_opt(self):

        REACTION_URL = "http://rest.kegg.jp/list/rn"

        Name_Info_opt_List = []

        try:
            Reaction_Info = urlopen(REACTION_URL, None, timeout=1000000)

            while True:
                Reaction_line = Reaction_Info.readline()
                if not Reaction_line: break
                Reaction_new_line = str(Reaction_line).split("\\t")

                Name_Info_opt_List.append(str(Reaction_new_line[1]).replace("\\n'","").replace('"','').strip())

                #print(Reaction_new_line[0])

        except HTTPError as e:
            print(e)
        except TimeoutError as e:
            print(e)
        except socket.timeout:
            print('timeout')
        except Exception as e:
            print(e)

        return Name_Info_opt_List


    #Reaction에 대한 모든 정보 가지고 옴
    def get_Reaction_All_Info(self, Reaction_code):

        Reaction_INFO_URL = "http://rest.kegg.jp/get/" + Reaction_code

        All_Info_List = []

        try:
            Reaction_Info = urlopen(Reaction_INFO_URL, None, timeout=1000000)

            while True:
                Reaction_line = Reaction_Info.readline()
                if not Reaction_line: break

                All_Info_List.append(Reaction_line)

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

    #Reaction에서 Name 정보 가지고 옴
    def get_Reaction_Name_Info(self, Reaction_code):

        Reaction_INFO_URL = "http://rest.kegg.jp/get/" + Reaction_code

        Temp_List = []
        Name_Info_List = []

        try:
            Reaction_Info = urlopen(Reaction_INFO_URL, None, timeout=1000000)

            while True:
                Reaction_line = Reaction_Info.readline()
                if not Reaction_line: break

                Temp_List.append(Reaction_line)

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


    #Reaction에서 Definition 정보 가지고 옴
    def get_Reaction_Definition_Info(self, Reaction_code):

        Reaction_INFO_URL = "http://rest.kegg.jp/get/" + Reaction_code

        Temp_List = []
        Definition_Info_List = []

        try:
            Reaction_Info = urlopen(Reaction_INFO_URL, None, timeout=1000000)

            while True:
                Reaction_line = Reaction_Info.readline()
                if not Reaction_line: break

                Temp_List.append(Reaction_line)

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

    #Reaction에서 Equation 정보 가지고 옴
    def get_Reaction_Equation_Info(self, Reaction_code):

        Reaction_INFO_URL = "http://rest.kegg.jp/get/" + Reaction_code

        Temp_List = []
        Equation_Info_List = []

        try:
            Reaction_Info = urlopen(Reaction_INFO_URL, None, timeout=1000000)

            while True:
                Reaction_line = Reaction_Info.readline()
                if not Reaction_line: break

                Temp_List.append(Reaction_line)

            for ai in Temp_List:
                if str(ai).__contains__("EQUATION"):
                    Equation_Info_List.append(str(str(ai).replace("b'EQUATION  ", "").replace('\\n', "").replace("'", "")).strip())

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

        return Equation_Info_List

    #Reaction에서 Comment 정보 가지고 옴
    def get_Reaction_Comment_Info(self, Reaction_code):

        Reaction_INFO_URL = "http://rest.kegg.jp/get/" + Reaction_code

        LineMarker = False
        Comment_Info_List = []

        try:
            Reaction_Info = urlopen(Reaction_INFO_URL, None, timeout=1000000)

            while True:
                Reaction_line = Reaction_Info.readline()
                if not Reaction_line: break

                if str(Reaction_line).__contains__("COMMENT"):
                    LineMarker = True
                elif str(Reaction_line).__contains__("RCLASS"):
                    LineMarker = False

                if LineMarker == True:
                    Comment_Info_List.append(str(str(Reaction_line).replace("b'COMMENT     ","").replace('\\n', "").replace("'", "").replace("b            ","")).strip())


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

        return Comment_Info_List

    #Reaction에서 Rclass 정보 가지고 옴
    def get_Reaction_Rclass_Info(self, Reaction_code):

        Reaction_INFO_URL = "http://rest.kegg.jp/get/" + Reaction_code

        LineMarker = False
        Rclass_Info_List = []

        try:
            Reaction_Info = urlopen(Reaction_INFO_URL, None, timeout=1000000)

            while True:
                Reaction_line = Reaction_Info.readline()
                if not Reaction_line: break

                if str(Reaction_line).__contains__("RCLASS"):
                    LineMarker = True
                elif str(Reaction_line).__contains__("ENZYME"):
                    LineMarker = False

                if LineMarker == True:
                    Rclass_Info_List.append(str(str(Reaction_line).replace("b'RCLASS      ","").replace('\\n', "").replace("'", "").replace("b            ","")).strip())


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

        return Rclass_Info_List

    #Reaction에서 Enzyme 정보 가지고 옴
    def get_Reaction_Enzyme_Info(self, Reaction_code):

        Reaction_INFO_URL = "http://rest.kegg.jp/get/" + Reaction_code

        LineMarker = False
        Enzyme_Info_List = []

        try:
            Reaction_Info = urlopen(Reaction_INFO_URL, None, timeout=1000000)

            while True:
                Reaction_line = Reaction_Info.readline()
                if not Reaction_line: break

                if str(Reaction_line).__contains__("ENZYME"):
                    LineMarker = True
                elif str(Reaction_line).__contains__("PATHWAY"):
                    LineMarker = False

                if LineMarker == True:
                    Enzyme_Info_List.append(str(str(Reaction_line).replace("b'ENZYME      ","").replace('\\n', "").replace("'", "").replace("b            ","")).strip())


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

    #Reaction에서 Pathway 정보 가지고 옴
    def get_Reaction_Pathway_Info(self, Reaction_code):

        Reaction_INFO_URL = "http://rest.kegg.jp/get/" + Reaction_code

        LineMarker = False
        Pathway_Info_List = []

        try:
            Reaction_Info = urlopen(Reaction_INFO_URL, None, timeout=1000000)

            while True:
                Reaction_line = Reaction_Info.readline()
                if not Reaction_line: break

                if str(Reaction_line).__contains__("PATHWAY"):
                    LineMarker = True
                elif str(Reaction_line).__contains__("ORTHOLOGY"):
                    LineMarker = False

                if LineMarker == True:
                    Pathway_Info_List.append(str(str(Reaction_line).replace("b'PATHWAY     ","").replace('\\n', "").replace("'", "").replace("b            ","")).strip())


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

    #Reaction에서 Orthology 정보 가지고 옴
    def get_Reaction_Orthology_Info(self, Reaction_code):

        Reaction_INFO_URL = "http://rest.kegg.jp/get/" + Reaction_code

        LineMarker = False
        Orthology_Info_List = []

        try:
            Reaction_Info = urlopen(Reaction_INFO_URL, None, timeout=1000000)

            while True:
                Reaction_line = Reaction_Info.readline()
                if not Reaction_line: break

                if str(Reaction_line).__contains__("ORTHOLOGY"):
                    LineMarker = True
                elif str(Reaction_line).__contains__("///") or str(Reaction_line).__contains__("DBLINKS"):
                    LineMarker = False

                if LineMarker == True:
                    Orthology_Info_List.append(str(str(Reaction_line).replace("b'ORTHOLOGY   ","").replace('\\n', "").replace("'", "").replace("b            ","")).strip())


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

        return Orthology_Info_List
