import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

EDC_CID = []

"""
# read ECD CID number file
f = open("", 'r')

while True:
    line = f.readline()
    if not line:break
    new_line = line.split("\t")
    EDC_CID.append(new_line[0].strip().replace('"',''))

print("Read EDC CID file")
"""
"""

EDC_CID = ["7456"]

for cid in EDC_CID:

    print(str("Input CID number: ") + str(cid).strip())

    #PubChem_URL = "https://pubchem.ncbi.nlm.nih.gov/compound/" + str(cid).strip() + "#section=CAS&fullscreen=true"
    #PubChem_URL = "https://pubchem.ncbi.nlm.nih.gov/compound/" + str(cid).strip()
    PubChem_URL = "https://pubchem.ncbi.nlm.nih.gov/compound/" + str(cid).strip() + "#section=Depositor-Supplied-Synonyms&fullscreen=true"

    CAS_Info = urlopen(PubChem_URL, None, timeout=1000000)

    while True:
        PubChem_line = CAS_Info.readline()
        if not PubChem_line:break

        print(PubChem_line)
"""

web_url = "https://pubchem.ncbi.nlm.nih.gov/compound/7456#section=CAS"

with urllib.request.urlopen(web_url) as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')


print(soup)