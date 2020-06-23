from urllib.request import urlopen
import re

URL = "http://www.knapsackfamily.com/knapsack_core/information.php?word=C00030000"

URL_Info = urlopen(URL, None, timeout=100000)

Key = False

while True:
    Info_line = URL_Info.readline()
    if not Info_line: break

    if str(Info_line).__contains__('''th class="inf"'''):
        Key = True
    if str(Info_line).__contains__('<tr>'):
        Key = False

    #KNApSAcK 주요 정보 뽑아내는 IF문
    #if str(Info_line).__contains__('''<th class="inf"'''):
    #    print(Info_line)
    #if str(Info_line).__contains__('''<td colspan="4"'''):
    #    print(Info_line)

    #KNApSAcK Biological resource 뽑아내는 IF문
    if str(Info_line).__contains__("<td class=org>"):
        print(str(Info_line).split('</td>'))