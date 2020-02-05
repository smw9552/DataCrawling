from KEGG_OOP.KEGG_Code import *
from KEGG_OOP.Protein import *
from KEGG_OOP.Disease import *
from KEGG_OOP.Pathway import *

KEGG_Code_List = KEGG_Code()
Pathway_List = Pathway()
Disease_List = Disease()
Protein_List = Protein()

All_KO_List = []
KO_link_Pathway_List = []
KO_link_Disease_List = []
KO_link_Protein_List = []
KO_link_Pathway_Cpd_List = []

#KEGG API에서 전체 KO 가지고 오는 경우
#All_KO_List = KEGG_Code_List.getAll_KO_Code("ko")

#KO 데이터를 input 형태로 넣어주는 경우
#KO 전체 데이터는 All_KO_List.csv에 포함
#전체 KO 중에서 protein, disease, pathway와 연결되는 KO 리스트만 Linked_KO_List.csv에 포함

f = open("C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\연구과제\\파로스공동연구\\GraphDB\Data\\KEGG_DB\\Linked_EC_KO_List.csv", 'r')

while True:
    line = f.readline()
    if not line:break
    new_line = line.split(",")
    All_KO_List.append(new_line[0].strip())

print("Input all KO list")
print(len(All_KO_List))


#KO와 연관된 pathway, disease, protein code를 KEGG API에서 가지고 오는 부분
for ai in All_KO_List:

    #KO_link_Pathway_List.append(Pathway_List.get_KO_PATHWAY_Link(str(ai)))
    #KO_link_Disease_List.append(Disease_List.get_KO_DISEASE_Link(str(ai)))
    KO_link_Protein_List.append(Protein_List.get_KO_EC_Link(str(ai)))

    print(ai + " link info adding")


#파일 작성 경로 (KO - Pathway_code - Pathway_information)
f = open ("C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\연구과제\\파로스공동연구\\GraphDB\\Data\\KEGG_DB\\All_Info\\EC_Cpd_code.txt", 'w')

#파일 작성 (KO - Pathway_code - Pathway information)
for bi in range(0, len(All_KO_List)):
    for ci in range(0, len(KO_link_Pathway_List[bi])):
        print("write KO =" + All_KO_List[bi])
        Data = str(All_KO_List[bi]) + "\t" + str(KO_link_Pathway_List[bi][ci].replace("['","").replace("']","")) + "\t" \
        + str(Pathway_List.get_Pathway_Name_Info(str(KO_link_Pathway_List[bi][ci]))).replace("['","").replace("']","") + "\t" \
        + str(Pathway_List.get_Pathway_Class_Info(str(KO_link_Pathway_List[bi][ci]))).replace("['","").replace("']","") + "\n"
        # + str(Pathway_List.get_Pathway_Disease_Info(str(KO_link_Pathway_List[bi][ci]))).replace("['","").replace("']", "").replace("'","") + "\n"
        # + str(Pathway_List.get_Pathway_Module_Info(str(KO_link_Pathway_List[bi][ci]))).replace("['","").replace("']", "").replace("'","") + "\n"

        f.write(Data)
f.close()
print("write KO-Pathway info file!!")


#파일 작성 경로 (KO - Disease_code - Disease_information)
f = open("C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\연구과제\\파로스공동연구\\GraphDB\\Data\\KEGG_DB\\All_Info\\Disease.txt", 'w')

#파일 작성 (KO - Disease_code - Disease_information)
for bi in range(0, len(All_KO_List)):
    for ci in range(0, len(KO_link_Disease_List[bi])):
        print("write KO =" + All_KO_List[bi])
        Data = str(All_KO_List[bi]) + "\t" + str(KO_link_Disease_List[bi][ci].replace("['","").replace("']","")) + "\t" \
        + str(Disease_List.get_Disease_Name_Info(str(KO_link_Disease_List[bi][ci]))).replace("['","").replace("']","") + "\t" \
        + str(Disease_List.get_Disease_Category_Info(str(KO_link_Disease_List[bi][ci]))).replace("['","").replace("']","") + "\n"
        #+ str(Disease_List.get_Disease_Description_Info(str(KO_link_Disease_List[bi][ci]))).replace("['","").replace("']", "").replace("'","") + "\t" \
        #+ str(Disease_List.get_Disease_Pathway_Info(str(KO_link_Disease_List[bi][ci]))).replace("['","").replace("']", "").replace("'","") + "\n"

        f.write(Data)
f.close()
print("write KO-Disease info file!!")


#파일 작성 경로 (KO - Protein_code - Protein_information)
f = open("C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\연구과제\\파로스공동연구\\GraphDB\\Data\\KEGG_DB\\All_Info\\Protein.txt", 'w')

#파일 작성 (KO - Protein_code - Protein_information)
for bi in range(0, len(All_KO_List)):
    for ci in range(0, len(KO_link_Protein_List[bi])):
        print("write KO =" + All_KO_List[bi])
        Data = str(All_KO_List[bi]) + "\t" + str(KO_link_Protein_List[bi][ci].replace("['","").replace("']","")) + "\t" \
        + str(Protein_List.get_EC_Name_Info(str(KO_link_Protein_List[bi][ci]))).replace("['","").replace("']","").replace("'","") + "\t" \
        + str(Protein_List.get_EC_Class_Info(str(KO_link_Protein_List[bi][ci]))).replace("['","").replace("']", "").replace("'","") + "\n"
        # + str(Protein_List.get_EC_CPD_code_Info(str(KO_link_Protein_List[bi][ci]))).replace("['","").replace("']","").replace("'","") + "\t" \
        #+ str(Protein_List.get_EC_Reaction_code_Info(str(KO_link_Protein_List[bi][ci]))).replace("['", "").replace("']","").replace("'", "") + "\n"


        #+ str(Protein_List.get_EC_Substrate_Info(str(KO_link_Protein_List[bi][ci]))).replace("['", "").replace("']","").replace("'", "") + "\t" \
        #+ str(Protein_List.get_EC_Product_Info(str(KO_link_Protein_List[bi][ci]))).replace("['", "").replace("']","").replace("'", "") + "\t" \
        #+ str(Protein_List.get_EC_Reaction_code_Info(str(KO_link_Protein_List[bi][ci]))).replace("['", "").replace("']","").replace("'", "")+ "\n"
        #+ str(Protein_List.get_EC_Reaction_eq_Info(str(KO_link_Protein_List[bi][ci]))).replace("['","").replace("']", "").replace("'","")+ "\n"


        f.write(Data)
f.close()
print("write KO-Protein info file!!")


#파일 작성 (KO - Protein_code - Cpd code)
f = open("C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\연구과제\\파로스공동연구\\GraphDB\\Data\\KEGG_DB\\All_Info\\KO_Pathway_Cpd_code.txt", 'w')


#파일 작성 (KO - Protein_code - Cpd_code) // KNAPSACK DB 데이터와 cpd code로 연결하기 위해서 데이터 작성하는 부분
for bi in range(0, len(All_KO_List)):
    for ci in range(0, len(KO_link_Protein_List[bi])):
        KO_link_Pathway_Cpd_List.append(Protein_List.get_EC_CPD_code_Info(str(KO_link_Protein_List[bi][ci])))

#print(KO_link_Pathway_Cpd_List)

for bi in range(0, len(All_KO_List)):
    print("write KO =" + All_KO_List[bi])
    for ci in range(0, len(KO_link_Pathway_Cpd_List[bi])):

        Data = str(All_KO_List[bi]) + "\t" + str(KO_link_Pathway_Cpd_List[bi][ci]).replace("['","").replace("']","").replace("'", "") + "\n"

        f.write(Data)
f.close()

print("write KO-Cpd code info file!!")