from urllib.request import urlretrieve

#Test download cid:2244
#urlretrieve("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/SDF", "C:\\Users\\hkjin\\Desktop\\Python_Calculation\\test.sdf")

#Read biocide CAS-CID number file
#[0]: Biocide CAS
#[1]: Biocide CID

########################
# Biocide sdf download #
########################

Biocide_CAS = []
Biocide_CID = []
InputFilePath = "C:\\Users\\hkjin\\Desktop\\Python_Calculation\\"
InputFileName = "Extract_CAS_CID_output_new_v2.txt"
SDF_OutputFilePath = "C:\\Users\\hkjin\\Desktop\\Python_Calculation\\Biocide_CID_SDF\\"

f = open(InputFilePath + InputFileName, "r")

while True:
    line = f.readline()
    if not line:break
    new_line = line.split("\t")
    Biocide_CAS.append(new_line[0].replace('"','').strip())
    Biocide_CID.append(new_line[1].replace('"','').strip())

print("Read Biocide CID")

#Pubchem SDF download

for ai in range(0, len(Biocide_CAS)):

    urlretrieve("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/" + str(Biocide_CID[ai]) + "/SDF",
                SDF_OutputFilePath + str(Biocide_CAS[ai] + ".SDF"))

    print(str("Download files: ") + str(Biocide_CAS[ai]))

print("download completed")


###############################################
# Compound sdf of AOP target protein download #
###############################################

CID = []
SDF_OutputFilePath = ""

f = open("C")


