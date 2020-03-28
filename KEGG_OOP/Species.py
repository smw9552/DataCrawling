from urllib.request import urlopen
from urllib.error import HTTPError
import socket

class Species:

    def get_Species_Name_Info(self):

        SPECIES_URL = "http://rest.kegg.jp/list/organism"

        Name_Info_List = []

        try:
            Species_Info = urlopen(SPECIES_URL, None, timeout=1000000)

            while True:
                Species_line = Species_Info.readline()
                if not Species_line: break

                Name_Info_List.append(str(Species_line[7:10]).replace("b'","").replace("'",""))

        except HTTPError as e:
            print(e)
        except TimeoutError as e:
            print(e)
        except socket.timeout:
            print('timeout')
        except Exception as e:
            print(e)

        return Name_Info_List

    def get_Species_Definition_Info(self):

        SPECIES_URL = "http://rest.kegg.jp/list/organism"

        Definition_Info_List = []

        try:
            Species_Info = urlopen(SPECIES_URL, None, timeout=1000000)

            while True:
                Species_line = Species_Info.readline()
                if not Species_line: break
                Species_new_line = str(Species_line).split("\\t")

                Definition_Info_List.append(Species_new_line[2].strip())

                print(Species_new_line[2].strip())

        except HTTPError as e:
            print(e)
        except TimeoutError as e:
            print(e)
        except socket.timeout:
            print('timeout')
        except Exception as e:
            print(e)

        return Definition_Info_List

    def get_Species_Taxonomy_Info(self):

        SPECIES_URL = "http://rest.kegg.jp/list/organism"

        Taxonomy_Info_List = []

        try:
            Species_Info = urlopen(SPECIES_URL, None, timeout=1000000)

            while True:
                Species_line = Species_Info.readline()
                if not Species_line: break
                Species_new_line = str(Species_line).split("\\t")

                Taxonomy_Info_List.append(Species_new_line[3].strip().replace("\\n","").replace("'",""))

                print(Species_new_line[3].strip().replace("\\n","").replace("'",""))

        except HTTPError as e:
            print(e)
        except TimeoutError as e:
            print(e)
        except socket.timeout:
            print('timeout')
        except Exception as e:
            print(e)

        return Taxonomy_Info_List