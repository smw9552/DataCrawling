from MeSH.Reader import MeSH_Reader
from MeSH.Reader import Data_Reader
from MeSH.Writer import Data_Writer
from MeSH.Finder import MeSH_Finder

#Define classes

MeSH_r = MeSH_Reader()
Data_r = Data_Reader()
MeSH_f = MeSH_Finder()
Data_w = Data_Writer()

FilePath = "C:\\Users\\seomy\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_process\\MeSH\\MeSH_desc_2020\\"
FileName = "desc2020.xml"

DataFilePath = "C:\\Users\\seomy\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_process\\HMDB\\"
DataFileName = "HMDB_Protein_Disease.txt"

OutputFilePath = "C:\\Users\\seomy\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_process\\HMDB\\"
OutputFileName = "HMDB_Protein_Disease_MeSH_mapping.txt"

#OutputFilePath_temp = "C:\\Users\\seomy\\Desktop\\"
#OutputFileName_temp = "MeSH_RawData.txt"


MeSH_All_Name = MeSH_r.get_All_MeSH_Concept_Term_Names(FilePath, FileName)
MeSH_Unique_ID = MeSH_r.get_All_MeSH_Unique_ID(FilePath, FileName)


print(len(MeSH_All_Name))
print(len(MeSH_Unique_ID))


#Input disease name 정보
Input_Disease_Name = Data_r.read_Disease_Name_txt(DataFilePath, DataFileName, 2)

#Test 데이터
#Test = ["liver diseases", "CANCER", "Neoplasms","Seo"]
#MeSH_Unique_ID_Mapping = MeSH_f.find_MeSH_Disease_Cocept_Term_To_ID(Test, MeSH_All_Name, MeSH_Unique_ID)
#Data_w.write_disease_to_id_file_txt(OutputFilePath, OutputFileName, Test, MeSH_Unique_ID_Mapping)

# Unique ID mapping
MeSH_Unique_ID_Mapping = MeSH_f.find_MeSH_Disease_Cocept_Term_To_ID(Input_Disease_Name, MeSH_All_Name, MeSH_Unique_ID)

# File write
Data_w.write_disease_to_id_file_txt(OutputFilePath, OutputFileName, Input_Disease_Name, MeSH_Unique_ID_Mapping)


"""
#Write MeSH raw data
Data_w.write_MeSH_Info_txt(OutputFilePath_temp, OutputFileName_temp, MeSH_All_Name, MeSH_Unique_ID)
"""