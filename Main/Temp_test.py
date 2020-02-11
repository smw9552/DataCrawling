from KEGG_OOP.Metabolite import *
from KEGG_OOP.Disease import *
from KEGG_OOP.KEGG_Orthology import *
from KEGG_OOP.Pathway import *
from KEGG_OOP.Protein import *
from KEGG_OOP.Reaction import *

DISEASE = Disease()


Disease_code = DISEASE.get_Disease_Name_Info_opt()

print(len(Disease_code))

for code in Disease_code:

    print(code)