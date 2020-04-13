from MeSH.Reader import MeSH_Reader
from MeSH.Reader import Data_Reader
from MeSH.Writer import Data_Writer
from MeSH.Finder import MeSH_Finder

#Define classes

MeSH_r = MeSH_Reader()
Data_r = Data_Reader()
MeSH_f = MeSH_Finder()
Data_w = Data_Writer()

FilePath = "C:\\Users\\Seomyungwon\\Desktop\\CORONet_Test\\"
FileName_desc = "desc2020.xml"
FileName_supp = "supp2020.xml"

DataFilePath = "C:\\Users\\Seomyungwon\\Desktop\\CORONet_Test\\"
DataFileName = "DrugBank_Input.txt"

OutputFilePath = "C:\\Users\\Seomyungwon\\Desktop\\CORONet_Test\\"
OutputFileName_desc = "DrugBank_MeSH_mapping_output_2020_desc.txt"
OutputFileName_supp = "DrugBank_MeSH_mapping_output_2020_supp.txt"

print("Load data")

#Read MeSH xml data
MeSH_All_Name_desc = MeSH_r.get_All_MeSH_Concept_Term_Names(FilePath, FileName_desc)
MeSH_Unique_ID_desc = MeSH_r.get_All_MeSH_Unique_ID(FilePath, FileName_desc)
MeSH_All_Name_supp = MeSH_r.get_All_MeSH_Concept_Term_Names_supp(FilePath, FileName_supp)
MeSH_Unique_ID_supp = MeSH_r.get_All_MeSH_Unique_ID_supp(FilePath, FileName_supp)

print("Read data")

print("length of desc xml")
print(len(MeSH_All_Name_desc))
print(len(MeSH_Unique_ID_desc))
print("\n")

print("length of supp xml")
print(len(MeSH_All_Name_supp))
print(len(MeSH_Unique_ID_supp))

#Input disease name 정보
Input_Disease_Name = Data_r.read_Disease_Name_txt(DataFilePath, DataFileName, 0)

#Test 데이터
#Test = ["liver diseases", "CANCER", "Neoplasms","Seo"]
#MeSH_Unique_ID_Mapping = MeSH_f.find_MeSH_Disease_Cocept_Term_To_ID(Test, MeSH_All_Name, MeSH_Unique_ID)
#Data_w.write_disease_to_id_file_txt(OutputFilePath, OutputFileName, Test, MeSH_Unique_ID_Mapping)

# Unique ID mapping
#MeSH_Unique_ID_Mapping_desc = MeSH_f.find_MeSH_Disease_Cocept_Term_To_ID(Input_Disease_Name, MeSH_All_Name_desc, MeSH_Unique_ID_desc)
MeSH_Unique_ID_Mapping_supp = MeSH_f.find_MeSH_Disease_Cocept_Term_To_ID(Input_Disease_Name, MeSH_All_Name_supp, MeSH_Unique_ID_supp)

print("ID mapping")

# File write
Data_w.write_disease_to_id_file_txt(OutputFilePath, OutputFileName_desc, Input_Disease_Name, MeSH_Unique_ID_Mapping_desc)
Data_w.write_disease_to_id_file_txt(OutputFilePath, OutputFileName_supp, Input_Disease_Name, MeSH_Unique_ID_Mapping_supp)

print("write file")

#Write MeSH raw data
#Data_w.write_MeSH_Info_txt(OutputFilePath_temp, OutputFileName_temp, MeSH_All_Name, MeSH_Unique_ID)