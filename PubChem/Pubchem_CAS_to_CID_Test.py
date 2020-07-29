from urllib.request import urlopen


Biocide_CAS = []


#read biocide compound CAS number file
f = open("C:\\Users\\hkjin\\Desktop\\Python_Calculation\\Extract_CAS_Number_v2.txt", 'r')

while True:
    line = f.readline()
    if not line:break
    new_line = line.split("\t")
    Biocide_CAS.append(new_line[0].strip())

print("Read CAS number files")



Pubchem_CID = []
Biocide_CAS_of_CID = []

for cas_num in Biocide_CAS:

    print(str("Input CAS number: ") + str(cas_num).strip())

    PubChem_URL = "https://pubchem.ncbi.nlm.nih.gov/compound/" + str(cas_num).strip()
    #PubChem_URL = "https://pubchem.ncbi.nlm.nih.gov/#query=compound/" + str(cas_num).strip()

    CID_Info = urlopen(PubChem_URL, None, timeout=100000)

    while True:
        PubChem_line = CID_Info.readline()
        if not PubChem_line: break

        if (str(PubChem_line).__contains__('''b'    <meta name="pubchem_uid_value"''')):


            Pubchem_CID.append(str(PubChem_line).
                  replace("b'","").
                  replace('"','').
                  replace("    <meta name=pubchem_uid_value content=","").
                  replace("'","").
                  replace(">","").
                  replace("\\n","").strip())

            Biocide_CAS_of_CID.append(cas_num)
            """
            print(str(PubChem_line).
                  replace("b'","").
                  replace('"','').
                  replace("    <meta name=pubchem_uid_value content=","").
                  replace("'","").
                  replace(">","").
                  replace("\\n","").strip())
            """


#print(len(Biocide_CAS))
#print(len(Pubchem_CID))


print("Extract CID number")

f_out = open("C:\\Users\\hkjin\\Desktop\\Python_Calculation\\Extract_CAS_CID_output_new_v2.txt", "w")

#Data = str("CAS") + "\t" + str("PubChem_CID") + "\n"
"""
for ai in range(0, len(Biocide_CAS)):

    Data = str(Biocide_CAS[ai]) + "\t" + str(Pubchem_CID[ai]) + "\n"
    f_out.write(Data)
"""
for bi in range(0, len(Pubchem_CID)):

    Data = str(Biocide_CAS_of_CID[bi]) + "\t" + str(Pubchem_CID[bi]) + "\n"
    f_out.write(Data)

f_out.close()
print("Write files")