from urllib.request import urlopen
from urllib.error import HTTPError
import socket


class Cell_line:

    def get_Cell_line_Definition(self):

        CELL_LINE_URL = "http://rest.kegg.jp/list/cell"

        Definition_Info_List = []

        try:
            Cell_line_Info = urlopen(CELL_LINE_URL, None, timeout=1000000)

            while True:
                Cell_line_line = Cell_line_Info.readline()
                if not Cell_line_line: break
                Cell_line_new_line = str(Cell_line_line).split("\\t")

                Definition_Info_List.append(str(Cell_line_new_line[1]).replace("\\n'","").strip())

#                print(str(Cell_line_new_line[1]).replace("\\n'","").strip()

        except HTTPError as e:
            print(e)
        except TimeoutError as e:
            print(e)
        except socket.timeout:
            print('timeout')
        except Exception as e:
            print(e)

        return Definition_Info_List


