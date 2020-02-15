word = ['a','e','x','Y']

MeSH_All_Name_list = [['a','b','c'], ['d','e','f'], ['g','h','i']]
MeSH_Unique_ID_list = ['D_1', 'D_2', 'D_3']
Temp = []
Final_Temp = []
final_test = []

for key in word:
    print(key)
    for info in MeSH_All_Name_list:

        if(info.__contains__(str(key))):
            Temp.append(MeSH_Unique_ID_list[MeSH_All_Name_list.index(info)])

        else:
            Temp.append(str("None"))

    Final_Temp.append(Temp)

    Temp = []

print(Final_Temp)


for data in Final_Temp:

    data = sorted(list(set(data)))

    print(data)

    if(len(data)>1):
        for info in data:
            if (info != str("None")):
                final_test.append(str(info))

    else:
        final_test.append("None")


print("Final")
print(final_test)

"""
        try:
            if(info.__contains__(str(key))):
                #Name이 포함된 list의 index 가지고 옴
                print(MeSH_All_Name_list.index(info))

                #Name와 id가 동일한 사이즈와 순서로 되어 있기 때문에 name의 index를 id에 적용하여 id 추출
                print(MeSH_Unique_ID_list[MeSH_All_Name_list.index(info)])

            #print(info.index(str(key)))
                Temp.append(MeSH_Unique_ID_list[MeSH_All_Name_list.index(info)])

        except ValueError:
            Temp.append(str("None"))

"""


"""
for data in Temp:
    if (data != str("None")):
        final_test.append(str(data))


#print(final_test)
"""