from KEGG_OOP.Disease import Disease

KEGG_Disease = Disease()

DataFilePath = "C:\\Users\\seomy\\Desktop\\KEGG_BRITE\\"
DataFileName = "KEGG_Disease_list_583.txt"

OutputFilePath = "C:\\Users\\seomy\\Desktop\\KEGG_BRITE\\"
OutputFileName = "KEGG_Disease_BRITE.txt"

f = open(DataFilePath + DataFileName, 'r', -1, 'utf-8')

Disease_ID = []

while True:
    line = f.readline()
    if not line:break
    new_line = line.split("\t")
    
    Disease_ID.append(str(new_line[0]).strip())

print("read Disease ID")
#Disease_ID = ['H02136', 'H01387']

Final_Disease_BRITE_Info = []

for ID in Disease_ID:
    Final_Disease_BRITE_Info.append(KEGG_Disease.get_Disease_BRITE_Info(ID))

Final_data_string = "KEGG_ID" + "\t" + "KEGG_BRITE" + "\n"

f = open(OutputFilePath + OutputFileName, 'w', -1, 'utf-8')

for ai in range(0,len(Disease_ID)):
    for BRITE in Final_Disease_BRITE_Info[ai]:

        Final_data_string = Final_data_string + str(Disease_ID[ai]) + "\t" + str(BRITE) + "\n"

f.write(Final_data_string)
f.close()

print("completed")