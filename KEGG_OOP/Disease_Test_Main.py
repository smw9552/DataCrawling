from KEGG_OOP.Disease import Disease


KEGG_Disease = Disease()

DataFilePath = "C:\\Users\\seomy\\Desktop\\"
DataFileName = "KEGG_Non-mapping_input.txt"

OutputFilePath = "C:\\Users\\seomy\\Desktop\\"
OutputFileName = "KEGG_non-mapping_output.txt"

f = open(DataFilePath + DataFileName, 'r')

Disease_code = []

while True:
    line = f.readline()
    if not line:break
    new_line = line.split("\t")

    Disease_code.append(str(new_line[0]).strip())


#Disease_code = ['H01946', 'H01942']

Final_data_string = "KEGG_ID" + "\t" + "MeSH_ID" + "\n"

f = open(OutputFilePath + OutputFileName, 'w')

for code in Disease_code:

    print(code)

    Final_data_string = Final_data_string + str(code) + "\t" \
                        + str(KEGG_Disease.get_Disease_MeSH_id_Info(code)) + "\n"


f.write(Final_data_string)
f.close()

print('completed')