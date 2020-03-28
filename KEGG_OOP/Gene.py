from urllib.request import urlopen
from urllib.error import HTTPError
import socket

class Gene:

    def get_Gene_Definition_Info(self):

        GENE_URL = "http://rest.kegg.jp/list/genome"

        Definition_Info_List = []

        try:
            Gene_Info = urlopen(GENE_URL, None, timeout=1000000)

            while True:
                Gene_line = Gene_Info.readline()
                if not Gene_line: break
                Gene_new_line = str(Gene_line).split("\\t")

                #print(Gene_new_line[1].replace("\\n'","").strip())
                Definition_Info_List.append(Gene_new_line[1].replace("\\n'","").strip())

        except HTTPError as e:
            print(e)
        except TimeoutError as e:
            print(e)
        except socket.timeout:
            print('timeout')
        except Exception as e:
            print(e)

        return Definition_Info_List