from KEGG_OOP.KEGG_Code import *
from KEGG_OOP.Pathway import *
from KEGG_OOP.Disease import *
from KEGG_OOP.Protein import *

KEGG_Code_List = KEGG_Code()
Pathway_Code_List = Pathway()
Disease_Code_List = Disease()
Protein_Code_List = Protein()

All_KO_List = []
KO_Link_Pathway_List = []
KO_Link_Disease_List = []
KO_Link_Protein_List = []

f = open("C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\연구과제\\파로스공동연구\\GraphDB\Data\\KEGG_DB\\All_KO_List.csv", 'r')

while True:
    line = f.readline()
    if not line:break
    new_line = line.split(",")
    All_KO_List.append(new_line[0].strip())

for a in All_KO_List:
    print(a)
"""

All_KO_List = KEGG_Code_List.getAll_KO_Code("ko")
#print(All_KO_List)

#Temp_KO_List = ["K00001", "K00002", "K00016"]
#print(Temp_KO_List)
print(len(All_KO_List))


for ai in All_KO_List:
    KO_Link_Pathway_List.append(Pathway_Code_List.get_KO_PATHWAY_Link(str(ai)))
    KO_Link_Disease_List.append(Disease_Code_List.get_KO_DISEASE_Link(str(ai)))
    KO_Link_Protein_List.append(Protein_Code_List.get_KO_EC_Link(str(ai)))
    print(ai + " adding")

#파일로 작성 (KO - Pathway_code - Pathway Name)
f = open("C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\연구과제\\파로스공동연구\\GraphDB\\Data\\KEGG_DB\\KO-PATHWAY.txt", 'w')

for bi in range(0, len(All_KO_List)):
   for ci in range(0, len(KO_Link_Pathway_List[bi])):
       Data = str(All_KO_List[bi]) + "\t" + str(KO_Link_Pathway_List[bi][ci]).replace("['","").replace("']","") + "\t" \
              + str(Pathway_Code_List.get_Pathway_Name_Info(str(KO_Link_Pathway_List[bi][ci]))).replace("['","").replace("']","") + "\n"
       f.write(Data)

f.close()
print("write KO-Pathway-Name file!")

#파일로 작성 (KO- EC_code - EC_Name)
f = open("C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\연구과제\\파로스공동연구\\GraphDB\\Data\\KEGG_DB\\KO-Protein.txt", 'w')

for bi in range(0, len(All_KO_List)):
   for ci in range(0, len(KO_Link_Protein_List[bi])):
       Data = str(All_KO_List[bi]) + "\t" + str(KO_Link_Protein_List[bi][ci]).replace("['","").replace("']","") + "\t" \
              + str(Protein_Code_List.get_EC_Name_Info(str(KO_Link_Protein_List[bi][ci]))).replace("['","").replace("']","") + "\n"
       f.write(Data)

f.close()
print("write KO-Protein-Name file!")

#파일로 작성 (KO- Disease_code - Disease_Name)
f = open("C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\연구과제\\파로스공동연구\\GraphDB\\Data\\KEGG_DB\\KO-Disease.txt", 'w')

for bi in range(0, len(All_KO_List)):
   for ci in range(0, len(KO_Link_Disease_List[bi])):
       Data = str(All_KO_List[bi]) + "\t" + str(KO_Link_Disease_List[bi][ci]).replace("['","").replace("']","") + "\t" \
              + str(Disease_Code_List.get_Disease_Name_Info(str(KO_Link_Disease_List[bi][ci]))).replace("['","").replace("']","") + "\n"
       f.write(Data)
f.close()
print("write KO-Disease-Name file!")

"""
"""
for bi in range(0,len(KO_Link_Pathway_List)):
    for ci in range(0, len(KO_Link_Pathway_List[bi])):
        KO_Link_Pathway_Name_List.append(Pathway_Code_List.get_Pathway_Name_Info(str(KO_Link_Pathway_List[bi][ci])))
        Dict_K0_Pathway_Name[Temp_KO_List[bi]] = Pathway_Code_List.get_Pathway_Name_Info(str(KO_Link_Pathway_Name_List[bi][ci]))

#print(KO_Link_Pathway_Name_List)

print(Dict_K0_Pathway_Name.keys())
print(Dict_K0_Pathway_Name.values())

#print(KEGG_Code_List.getAll_KO_Code("ko"))
#print(len(KEGG_Code_List.getAll_KO_Code("ko")))

#print(KEGG_Code_List.getAll_Disease_Code("disease"))
#print(KEGG_Code_List.getAll_Pathway_Code("pathway"))
#print(len(KEGG_Code_List.getAll_Pathway_Code("pathway")))

#print(Pathway_Code_List.get_KO_PATHWAY_Link("K00001"))

#print(Pathway_Code_List.get_PATHWAY_All_Info("map00010"))

print(Dict_K0_Pathway_Name['K00002'])
print(Dict_K0_Pathway_Name['K00003'])
"""

"""
f = open("C:\\Users\\Seomyungwon\\Desktop\\연습.txt", 'w')

for i in range(0, len(Dict_K0_Pathway_Name)):
    data = str(Temp_KO_List[i]).replace("['","").replace("']","") + "\t" + str(Dict_K0_Pathway_Name[str(Temp_KO_List[i])]) + "\t"
#    data = str(i).replace("['","").replace("']","") + str("\n")
    f.write(data)
"""