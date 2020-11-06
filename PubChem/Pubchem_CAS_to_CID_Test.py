from urllib.error import HTTPError
from urllib.request import urlopen


Data = []
Biocide_CAS = []
Biocide_Err = []

#read biocide compound CAS number file
f = open("C:\\Users\\hkjin\\Desktop\\Test\\CAS.txt", 'r')

while True:
    line = f.readline()
    if not line:break
    new_line = line.split("\t")
    Data.append(new_line[0].strip())

print("Read CAS number files")

#CAS number check
for d in Data:
    if(d.__contains__("-")):
        Biocide_CAS.append(d)

    else:
        Biocide_Err.append(d)

Pubchem_CID = []

for cas_num in Biocide_CAS:

    try:
        Label = True

        print(str("Input CAS number: ") + str(cas_num).strip())

        PubChem_URL = "https://pubchem.ncbi.nlm.nih.gov/compound/" + str(cas_num).strip()
        # PubChem_URL = "https://pubchem.ncbi.nlm.nih.gov/#query=compound/" + str(cas_num).strip()

        CID_Info = urlopen(PubChem_URL, None, timeout=100000)

        while True:
            PubChem_line = CID_Info.readline()
            if not PubChem_line: break

            # print(PubChem_line)

            if (str(PubChem_line).__contains__('''b'    <meta name="pubchem_uid_value"''')):
                Pubchem_CID.append(str(PubChem_line).
                                   replace("b'", "").
                                   replace('"', '').
                                   replace("    <meta name=pubchem_uid_value content=", "").
                                   replace("'", "").
                                 replace(">", "").
                                 replace("\\n", "").strip())

            # print(str(PubChem_line).
            #      replace("b'","").
            #      replace('"','').
            #      replace("    <meta name=pubchem_uid_value content=","").
            #      replace("'","").
            #      replace(">","").
            #      replace("\\n","").strip())

                Label = False
                break

        if (Label):
            Pubchem_CID.append("None")


    except HTTPError as e:
        print(e)
        Pubchem_CID.append("None")




#print(len(Biocide_CAS))
#print(len(Pubchem_CID))


print("Extract CID number")

#f_out = open("C:\\Users\\hkjin\\Google 드라이브\\과제\\생활화학제품\\EDC_library_data\\TOXCAST\\#HTS Data for ER Model\\ER Model release version 2015-08-28\\ER Model release version 2015-08-28\\sdf\\ER_Model_CAS_CID.txt", "w")
f_out = open("C:\\Users\\hkjin\\Desktop\\Test\\CID.txt","w")
#Data = str("Biocide_CAS") + "\t" + str("PubChem_CID") + "\n"

for ai in range(0, len(Pubchem_CID)):

    Data = str(Biocide_CAS[ai]) + "\t" + str(Pubchem_CID[ai]) + "\n"
    f_out.write(Data)

f_out.close()
print("Write files")