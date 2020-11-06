import socket
import urllib
from urllib.error import HTTPError, URLError
from urllib.request import urlretrieve

#Test download cid:2244
#urlretrieve("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/SDF", "C:\\Users\\hkjin\\Desktop\\Python_Calculation\\test.sdf")

#Read biocide CAS-CID number file
#[0]: Biocide CAS
#[1]: Biocide CID

########################
# Biocide sdf download #
########################

Chemical_CID = []
CAS = []
#Chemical_activity = []
InputFilePath = "C:\\Users\\hkjin\\Desktop\\Test\\"
InputFileName = "CID.txt"
SDF_OutputFilePath = "C:\\Users\\hkjin\\Desktop\\Test\\SDF\\"

f = open(InputFilePath + InputFileName, "r")

while True:
    line = f.readline()
    if not line:break
    new_line = line.split("\t")
    CAS.append(new_line[0].replace('"','').strip())
    Chemical_CID.append(new_line[1].replace('"','').strip())
    #Chemical_activity.append(new_line[1].replace('"','').strip())

print("Read Biocide CID")

print(Chemical_CID)
#print(Chemical_activity)

    #Pubchem SDF download
for ai in range(0, len(Chemical_CID)):

    try:

        if (str(Chemical_CID[ai]) == "None"):

            print("None CID")

        else:
            urlretrieve("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/" + str(Chemical_CID[ai]) + "/SDF",SDF_OutputFilePath + str(CAS[ai] + ".sdf"))
            print(str("Download files: ") + str(Chemical_CID[ai]))

    except socket.timeout:
        print("timeout")

    except TimeoutError as e:
        print("Timeout")

    except ConnectionResetError as e:
        print("Conncetion error")

    except HTTPError as e:
        print("HTTP Error")

    except URLError as e:
        print("URLError")

print("download completed")



"""
###############################################
# Compound sdf of AOP target protein download #
###############################################

CID = []
InputFilePath = "C:\\Users\\hkjin\\Desktop\\Python_Calculation\\"
InputFileName = "PPAR-g_Inactive_2.txt"
SDF_OutputFilePath = "C:\\Users\\hkjin\\Desktop\\Python_Calculation\\PPAR-g_SDF\\Inactive\\"

f = open(InputFilePath + InputFileName, "r")


while True:
    line = f.readline()
    if not line:break
    new_line = line.split("\t")
    CID.append(new_line[0].replace('"','').strip())

print("Read CID of bioassay")


for ai in range(0, len(CID)):

    try:

        #socket.setdefaulttimeout(1000)
        urlretrieve("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/" + str(CID[ai]) + "/SDF", SDF_OutputFilePath + str(CID[ai] + ".SDF"))

        print(str("Download files: ") + str(CID[ai]))

    except socket.timeout:
        print("timeout")

    except TimeoutError as e:
        print("Timeout")

    except ConnectionResetError as e:
        print("Conncetion error")

    except HTTPError as e:
        print("HTTP Error")

print("download completed")
"""