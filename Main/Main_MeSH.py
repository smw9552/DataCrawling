from MeSH.Reader import MeSH_Reader
from MeSH.Finder import MeSH_Finder

MeSH_r = MeSH_Reader()
MeSH_f = MeSH_Finder()

FilePath = "C:\\Users\\Seomyungwon\\DataCrawling\\Data\\"
FileName = "MeSH_xml_2020.xml"

All_MeSH_Name = []
#All_MeSH_Unique_ID = []
#Final_MeSH_Unique_ID = []

#Test = ["Eumycetoma", "Liver Diseases"]

All_MeSH_Terms = MeSH_r.get_All_MeSH_Terms(FilePath, FileName)
#All_MeSH_Unique_ID = MeSH_r.get_All_MeSH_UniqueID(FilePath, FileName)

print(All_MeSH_Terms)
#print(All_MeSH_Unique_ID)


#Final_MeSH_Unique_ID = MeSH_f.find_MeSH_Diseaes_Name_To_ID(Test, All_MeSH_Name, All_MeSH_Unique_ID)

#print(Final_MeSH_Unique_ID)


