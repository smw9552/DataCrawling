from KEGG_OOP.Metabolite import *
from KEGG_OOP.Disease import *
from KEGG_OOP.KEGG_Orthology import *
from KEGG_OOP.Pathway import *
from KEGG_OOP.Protein import *
from KEGG_OOP.Reaction import *

DISEASE = Disease()
METABOLITE = Metabolite()
KO = KEGG_Orthology()
PATHWAY = Pathway()
PROTEIN = Protein()
REACTION = Reaction()

#METABOLITE.get_Metabolite_Name_opt()
#Disease_List = DISEASE.get_Disease_Name_Info_opt()
#KO_List = KO.get_KO_Definition_Info_opt()
#list = PATHWAY.get_Pathway_Name_Info_opt()
#list = PROTEIN.get_EC_Name_Info_opt()

list = REACTION.get_Reaction_Name_Info_opt()

print(len(list))

for info in range(0, 1):
    print(list[info])