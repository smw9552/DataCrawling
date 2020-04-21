from MeSH.Reader import MeSH_Reader
from MeSH.Reader import Data_Reader
from MeSH.Writer import Data_Writer
from MeSH.Finder import MeSH_Finder

#Define classes

MeSH_r = MeSH_Reader()
Data_r = Data_Reader()
MeSH_f = MeSH_Finder()
Data_w = Data_Writer()

MeSH_FilePath = ""
MeSH_FileName_desc = ""

DataFilePath = ""
DataFileName = ""

OutputFilePath = ""
OutputFileName_desc = ""
OutputFileName_supp = ""

print ("Load data")

#Read MeSH_desc xml_data
MeSH_All_Name_desc = MeSH_r.get_All_MeSH_Concept_Term_Names(MeSH_FilePath, MeSH_FileName_desc)
MeSH_Unique_ID_desc = MeSH_r.get_All_MeSH_Unique_ID(MeSH_FilePath, MeSH_FileName_desc)

#Input name data
Input_Name = Data_r.read_Disease_Name_txt()










FileSplit_cnt = 10000

for ai in range(0, 26):

    MeSH_FileName_supp = str("supp2020_") + str(FileSplit_cnt) + str(".xml")
