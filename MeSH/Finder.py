class MeSH_Finder:

    # Keyword를 MeSH concept, term과 모두 비교하여 Unique id 추출
    def find_MeSH_Disease_Cocept_Term_To_ID(self, Keyword, MeSH_All_Name_list, MeSH_Unique_ID_list):

        Final_Unique_ID = []
        Temp = []
        Final_Temp = []

        for word in Keyword:

            for info_list in MeSH_All_Name_list:

                #MeSH Name list들을 하나씩 가져와서 list 내부에 word 값의 여부 조건
                if(info_list.__contains__(str(word).lower().strip())):
                    #MeSH Name list 내부에 word값이 있다면, word 값이 포함된 name list를 index를 가지고 옴
                    #MeSh Name list의 index 값으로 Unique ID 값 추출
                    Temp.append(MeSH_Unique_ID_list[MeSH_All_Name_list.index(info_list)])

                #MeSH Name list 내부에 word 값이 없는 경우 모두 "None" 처리 됨
                else:
                    Temp.append(str("None"))

            Final_Temp.append(Temp)

            #초기화 작업
            Temp = []

        for data in Final_Temp:

            #내부에 포함된 데이터들 (Unique ID, "None")의 중복을 제거하고 순서대로 정렬
            data = sorted(list(set(data)))

            #Unique ID를 포함하는 data를 필터하는 조건
            if (len(data)>1):
                #Unique id를 포함하는 리스트 내부에서 None 값을 제외하고 id만 추출하여 정리하는 작업
                for info in data:
                    if (info != str("None")):
                        Final_Unique_ID.append(str(info))

            #Unique ID를 포함하지 않는 경우에는 최종적으로 "None"으로 데이터 처리됨
            else:
                Final_Unique_ID.append(str("None"))


        return Final_Unique_ID



    # Keyword를 MeSH Heading name과 비교하여 Unique id 추출
    def find_MeSH_Diseaes_Name_To_ID(self, Keyword, MeSH_All_Name_list, MeSH_All_ID_list):

        Find_Unique_ID = []

        for word in Keyword:
            #print(word)

            try:
               #if (MeSH_All_Name_list.__contains__(str(word).lower())):
                Find_Unique_ID.append(MeSH_All_ID_list[MeSH_All_Name_list.index(str(word).lower().strip())])
            except ValueError:
                Find_Unique_ID.append(str("None_ID"))

        return Find_Unique_ID







