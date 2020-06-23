from MeSH.Reader import MeSH_Reader
from MeSH.Reader import Data_Reader
from MeSH.Writer import Data_Writer
from MeSH.Finder import MeSH_Finder

#Define classes

MeSH_r = MeSH_Reader()
Data_r = Data_Reader()
MeSH_f = MeSH_Finder()
Data_w = Data_Writer()

MeSH_FilePath_desc = "C:\\Users\\Seomyungwon\\Desktop\\CORONet_Test\\"
MeSH_FileName_desc = "desc2020.xml"

MeSH_FilePath_supp = "C:\\Users\\Seomyungwon\\Desktop\\CORONet_Test\\supp_xml_split\\"

DataFilePath = "C:\\Users\\Seomyungwon\\Desktop\\CORONet_Test\\"
DataFileName = "DrugBank_Input.txt"

OutputFilePath_desc = "C:\\Users\\Seomyungwon\\Desktop\\CORONet_Test\\Output\\"
OutputFileName_desc = "DrugBank_Mapping_output_desc.txt"

OutputFilePath_supp = "C:\\Users\\Seomyungwon\\Desktop\\CORONet_Test\\Output\\"

print ("Load data")
# Input name data
Input_Name = Data_r.read_Txt(DataFilePath, DataFileName, 0)


## [MeSH xml desc data]

# Read MeSH desc xml data
MeSH_All_Name_desc = MeSH_r.get_All_MeSH_Concept_Term_Names(MeSH_FilePath_desc, MeSH_FileName_desc)
MeSH_Unique_ID_desc = MeSH_r.get_All_MeSH_Unique_ID(MeSH_FilePath_desc, MeSH_FileName_desc)

# Unique ID mapping (MeSH desc xml data)
MeSH_Unique_ID_Mapping_desc = MeSH_f.find_MeSH_Chemical_Cocept_Term_To_ID(Input_Name, MeSH_All_Name_desc, MeSH_Unique_ID_desc)

print ("Unique ID mapping desc data")

# File write (MeSH desc xml data)
Data_w.write_chemical_to_id_file_txt(OutputFilePath_desc, OutputFileName_desc, Input_Name, MeSH_Unique_ID_Mapping_desc)


## [MeSH xml supplementary data]

FileSplit_cnt = 10000

for ai in range(0, 26):

    # Read MeSH supp xml data
    MeSH_FileName_supp = str("supp2020_") + str(FileSplit_cnt) + str(".xml")
    OutputFileName_supp = str("DrugBank_Mapping_output_xml_") + str(FileSplit_cnt) + str(".txt")

    MeSH_All_Name_supp = MeSH_r.get_All_MeSH_Concept_Term_Names_supp(MeSH_FilePath_supp, MeSH_FileName_supp)
    MeSH_Unique_ID_supp = MeSH_r.get_All_MeSH_Unique_ID_supp(MeSH_FilePath_supp, MeSH_FileName_supp)

    FileSplit_cnt = FileSplit_cnt + 10000

    # Unique ID mapping (MeSH supp xml data)
    MeSH_Unique_ID_Mapping_supp = MeSH_f.find_MeSH_Chemical_Cocept_Term_To_ID(Input_Name, MeSH_All_Name_supp, MeSH_Unique_ID_supp)

    print("Unique id mapping supp data")

    # File write (MeSH supp xml data)
    Data_w.write_chemical_to_id_file_txt(OutputFilePath_supp, OutputFileName_supp)








