from KEGG_OOP.Protein import *
from KEGG_OOP.Metabolite import *
from KEGG_OOP.KEGG_Code import *

ENTRY = KEGG_Code()
PROTEIN = Protein()
METABOLITE = Metabolite()


FilePath = "C:\\Users\\Seomyungwon\\Desktop\\KEGG_Crawling_New\\"
PROTEIN_File_Name = "Protein_New.txt"
METABOLITE_File_Name = "Metabolite_New.txt"

All_Protein_List = []

f = open("C:\\Users\\Seomyungwon\\Desktop\\KEGG_Crawling_New\\Protein_EntryList.txt",'r')
while True:
    line= f.readline()
    if not line: break
    new_line = line.split("\t")
    All_Protein_List.append(new_line[0].strip())

print("Input all Protein List")
print(len(All_Protein_List))

PROTEIN_f = open(FilePath + PROTEIN_File_Name, 'w')

for ai in All_Protein_List:

    PROTEIN_Data = str(ai).strip() + "\t" \
                   + str(PROTEIN.get_EC_Name_Info(str(ai))).replace("['","").replace("']","").replace("'","").strip() + "\t"\
                   + str(PROTEIN.get_EC_Class_Info(str(ai))).replace("['","").replace("']","").replace("'","").strip() + "\n"

    PROTEIN_f.write(PROTEIN_Data)

PROTEIN_f.close()
print("Write file related to the PROTEIN information")

# Metabolite 관련 데이터 정리 (Entry, Name, Formula, MW)
Metabolite_List = ENTRY.getAll_Metabolite_Entry()
METABOLITE_f = open(FilePath + METABOLITE_File_Name,'w')

for fi in range(0, len(Metabolite_List)):
    METABOLITE_Data = str(Metabolite_List[fi]).strip() + "\t" \
                + str(METABOLITE.get_Metabolite_Name_Info(Metabolite_List[fi])).replace("['","").replace("']","").replace("'","").strip() + "\t" \
                + str(METABOLITE.get_Metabolite_Formula_Info(Metabolite_List[fi])).replace("['","").replace("']","").replace("'","").strip() + "\t" \
                + str(METABOLITE.get_Metabolite_Molecular_Weight_Info(Metabolite_List[fi])).replace("['","").replace("']","").replace("'","").strip() + "\n"
    METABOLITE_f.write(METABOLITE_Data)

METABOLITE_f.close()
print("Write file related to the METABOLITE information")