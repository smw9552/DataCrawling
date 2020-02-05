from COCONUT_OOP.Functional_Food import *
from COCONUT_OOP.Herb import *
from COCONUT_OOP.Phenotype import *
from COCONUT_OOP.Prescription import *

#class
FOOD = Functional_Food()
HERB = Herb()
PHENOTYPE = Phenotype()
PRESCRIPTION = Prescription()

# The number of records
#-Functional food = 1~1615
#-Herb = 1~8492
#-Phenotype = 1~18482
#-Prescription = 1~20259

# File path & name
FilePath = "C:\\Users\\Seomyungwon\\Desktop\\COCONUT_Crawling_New\\"
FOOD_File_Name = "COCONUT_Food.txt"
HERB_File_Name = "COCONUT_Herb.txt"
PHENOTYPE_File_Name = "COCONUT_Phenotype.txt"
PRESCRIPTION_File_Name = "COCONUT_Prescription.txt"

#Functional food 관련 데이터 정리 (Name, Function)

FOOD_f = open(FilePath+FOOD_File_Name, 'w')

for ai in range(1, 1615):
    FOOD_Data = str(ai).strip() + "\t" \
                + str(FOOD.get_Functional_Food_Name(str(ai))).replace("['","").replace("']","").replace("'","").strip() + "\t"\
                + str(FOOD.get_Functional_Food_Function(str(ai))).replace("['","").replace("']","").replace("'","").strip() + "\n"

    FOOD_f.write(FOOD_Data)

FOOD_f.close()
print("Write file related to the Functional Food information")


# Herb 관련 데이터 정리 (Name, Function)
HERB_f = open(FilePath+HERB_File_Name, 'w')

for bi in range(1, 8492):
    HERB_Data = str(bi).strip() + "\t" \
                + str(HERB.get_Herb_Name(str(bi))).replace("['", "").replace("']", "").replace("'","").strip() + "\t" \
                + str(HERB.get_Herb_Function(str(bi))).replace("['", "").replace("']", "").replace("'","").strip() + "\n"

    HERB_f.write(HERB_Data)

HERB_f.close()
print("Write file related to the Herb information")


# Phenotype 관련 데이터 정리 (Name, Semantic type)
PHENOTYPE_f = open(FilePath+PHENOTYPE_File_Name, 'w')

for ci in range(1, 18482):
    PHENOTYPE_Data = str(ci).strip() + "\t" \
                + str(PHENOTYPE.get_Phenotype_Name(str(ci))).replace("['", "").replace("']", "").replace("'","").strip() + "\t" \
                + str(PHENOTYPE.get_Phenotype_Semantic_type(str(ci))).replace("['", "").replace("']", "").replace("'","").strip() + "\n"

    PHENOTYPE_f.write(PHENOTYPE_Data)

HERB_f.close()
print("Write file related to the Phenotype information")


# Prescription 관련 데이터 정리 (Name, Function, Precaution)
PRESCRIPTION_f = open(FilePath+PRESCRIPTION_File_Name, 'w')

for di in range(1, 20259):
    PRESCRIPTION_Data = str(di).strip() + "\t" \
                + str(PRESCRIPTION.get_Prescription_Name(str(di))).replace("['", "").replace("']", "").replace("'","").strip() + "\t" \
                + str(PRESCRIPTION.get_Prescription_Function(str(di))).replace("['", "").replace("']", "").replace("'","").strip() + "\t" \
                + str(PRESCRIPTION.get_Prescription_Precaution(str(di))).replace("['", "").replace("']", "").replace("'","").strip() + "\n"

    PRESCRIPTION_f.write(PRESCRIPTION_Data)

PRESCRIPTION_f.close()
print("Write file related to the Prescription information")