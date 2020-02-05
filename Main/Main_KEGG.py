from KEGG_OOP.KEGG_Code import *
from KEGG_OOP.KEGG_Orthology import *
from KEGG_OOP.Disease import *
from KEGG_OOP.Pathway import *
from KEGG_OOP.Protein import *
from KEGG_OOP.Reaction import *
from KEGG_OOP.Metabolite import *

# class
ENTRY = KEGG_Code()
KO = KEGG_Orthology()
DISEASE = Disease()
PATHWAY = Pathway()
PROTEIN = Protein()
REACTION = Reaction()
METABOLITE = Metabolite()

# File path & name
FilePath = "C:\\Users\\Seomyungwon\\Desktop\\KEGG_Crawling_New\\"
KO_File_Name = "KO.txt"
DISEASE_File_Name = "Disease.txt"
PATHWAY_File_Name = "Pathway.txt"
PROTEIN_File_Name = "Protein.txt"
REACTION_File_Name = "Reaction.txt"
METABOLITE_File_Name = "Metabolite.txt"


# KO 관련 데이터 정리 (Entry, Name, Definition)
KO_List = ENTRY.getAll_KO_Entry()
KO_f = open(FilePath + KO_File_Name, 'w')

for ai in range(0, len(KO_List)):
    KO_Data = str(KO_List[ai]).strip() + "\t" \
           + str(KO.get_KO_Name_Info(KO_List[ai])).replace("['","").replace("']","").strip() + "\t" \
           + str(KO.get_KO_Definition_Info(KO_List[ai])).replace("['","").replace("']","").strip() + "\n"
    KO_f.write(KO_Data)

KO_f.close()
print("Write file related to the KO information")

# Disease 관련 데이터 정리 (Entry, Name, Category)
Disease_List = ENTRY.getAll_Disease_Entry()
DISEASE_f = open(FilePath + DISEASE_File_Name, 'w')

for bi in range (0, len(Disease_List)):
    DISEASE_Data = str(Disease_List[bi]).strip() + "\t" \
                + str(DISEASE.get_Disease_Name_Info(Disease_List[bi])).replace("['","").replace("']","").strip() + "\t" \
                + str(DISEASE.get_Disease_Category_Info(Disease_List[bi])).replace("['","").replace("']","").strip() + "\n"

    DISEASE_f.write(DISEASE_Data)

DISEASE_f.close()
print("Write file related to the DISEASE information")

# Pathway 관련 데이터 정리 (Entry, Name, Class)
Pathway_List = ENTRY.getAll_Pathway_Entry()
PATHWAY_f = open(FilePath + PATHWAY_File_Name,'w')

for ci in range (0, len(Pathway_List)):
    PATHWAY_Data = str(Pathway_List[ci]).strip() + "\t" \
                + str(PATHWAY.get_Pathway_Name_Info(Pathway_List[ci])).replace("['","").replace("']","").strip() + "\t" \
                + str(PATHWAY.get_Pathway_Class_Info(Pathway_List[ci])).replace("['","").replace("']","").strip() + "\n"

    PATHWAY_f.write(PATHWAY_Data)

PATHWAY_f.close()
print("Write file related to the PATHWAY information")

# Protein 관련 데이터 정리 (Entry, Name, Class)
Protein_List = ENTRY.getAll_EC_Protein_Entry()
PROTEIN_f = open (FilePath + PROTEIN_File_Name,'w')

for di in range (0, len(Protein_List)):
    PROTEIN_Data = str(Protein_List[di]).strip() + "\t" \
                + str(PROTEIN.get_EC_Name_Info(Protein_List[di])).replace("['","").replace("']","").replace("'","").strip() + "\t" \
                + str(PROTEIN.get_EC_Class_Info(Protein_List[di])).replace("['","").replace("']","").replace("'","").strip() + "\n"

    PROTEIN_f.write(PROTEIN_Data)

PROTEIN_f.close()
print("Write file related to the PROTEIN information")

# Reaction 관련 데이터 정리 (Entry, Name, Definition, Equation)
Reaction_List = ENTRY.getAll_Reaction_Entry()
REACTION_f = open (FilePath + REACTION_File_Name,'w')

for ei in range (0, len(Reaction_List)):
     REACTION_Data = str(Reaction_List[ei]).strip() + "\t" \
                 + str(REACTION.get_Reaction_Name_Info(Reaction_List[ei])).replace("['","").replace("']","").replace("'","").strip() + "\t" \
                 + str(REACTION.get_Reaction_Definition_Info(Reaction_List[ei])).replace("['","").replace("']","").replace("'","").strip() + "\t" \
                 + str(REACTION.get_Reaction_Equation_Info(Reaction_List[ei])).replace("['","").replace("']","").replace("'","").strip() + "\n"
     REACTION_f.write(REACTION_Data)

REACTION_f.close()
print("Write file related to the REACTION information")

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