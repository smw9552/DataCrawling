import urllib.request
from socket import socket
from urllib.error import HTTPError

InputFilePath = "C:\\Users\\seomy\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\Data\\DB_data_process\\KEGG_DB\\KEGG_Drug\\"
InputFileName = "Drug_List.txt"

OutputFilePath = "C:\\Users\\seomy\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\Data\\DB_data_process\\KEGG_DB\KEGG_Drug\\SDF\\"

f = open (InputFilePath + InputFileName, 'r')


Drug_code = []
Drug_name = []

while True:
    line = f.readline()
    if not line:break
    new_line = line.split("\t")

    Drug_code.append(str(new_line[0]).strip())
    Drug_name.append(str(new_line[1]).strip())

for ai in range(0, len(Drug_code)):

    DRUG_STR_URL = "https://www.kegg.jp/dbget-bin/www_bget?-f+m+drug+" + str(Drug_code[ai])

    try:

        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'
                                 'AppleWebKit/537.11 (KHTML, like Gecko) '
                                 'Chrome/23.0.1271.64 Safari/537.11',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                   'Accept-Encoding': 'none',
                   'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}

        req = urllib.request.Request(DRUG_STR_URL, headers=headers)
        response = urllib.request.urlopen(req).read()

        text = response.decode('utf-8')
        Drug_f = open(OutputFilePath + str(Drug_code[ai] + str(".sdf")), 'w')
        Drug_f.write(text)
        Drug_f.close()
        print(str(Drug_code[ai]))
        print("write KEGG drug structure")

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


