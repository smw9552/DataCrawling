import xml.etree.ElementTree as ET

class Data_Reader:

    def read_Txt(self, DataFilePath, DataFileName, col_num):

        f = open(DataFilePath+DataFileName, 'r')

        Data = []

        while True:
            line = f.readline()
            if not line:break
            new_line = line.split("\t")

            Data.append(str(new_line[col_num]).lower().strip())

        return Data

    def read_Disease_Name_txt(self, DataFilePath, DataFileName, col_num):

        f = open(DataFilePath+DataFileName, 'r')

        Disease_Name = []

        while True:
            line = f.readline()
            if not line:break
            new_line = line.split("\t")

            Disease_Name.append(str(new_line[col_num]).lower().strip())

        return Disease_Name

class MeSH_Reader:

    # MeSH에서 제공하는 전체 MeSH heading에서 해당 되는 name 정보, concept 정보, Term 정보 모두 합쳐서 정리
    # 정보를 합쳐서 name으로 검색하는 경우 name과 관련된 모든 정보를 놓치지 않고 정리하기 위해 사용
    def get_All_MeSH_Concept_Term_Names(self, FilePath, FileName):

        doc = ET.parse(FilePath+FileName)
        root = doc.getroot()

        DescriptorRecord_tag = root.findall("DescriptorRecord")

        MeSH_All_Concept_Term_Name_list = []
        Temp_name = []
        Temp_concept = []
        Temp_term = []

        for record_cnt in range(0, len(DescriptorRecord_tag)):

            for name in DescriptorRecord_tag[record_cnt].iter("DescriptorName"):
                Temp_name.append(str(name.findtext("String")).lower().strip())

            for concept in DescriptorRecord_tag[record_cnt].iter("ConceptName"):
                Temp_concept.append(str(concept.findtext("String")).lower().strip())

            for term in DescriptorRecord_tag[record_cnt].iter("Term"):
                Temp_term.append(str(term.findtext("String")).lower().strip())

            #print("Term list")
            #print(Temp_term)

            Temp = Temp_name + Temp_concept + Temp_term
            # 중복 제거
            Temp = list(set(Temp))

            MeSH_All_Concept_Term_Name_list.append(Temp)

            # 초기화 작업
            Temp_concept = []
            Temp_term = []

        return MeSH_All_Concept_Term_Name_list


    # Input MeSH 파일 내에 있는 MeSH Heading의 해당되는 Unique id만 추출
    def get_All_MeSH_Unique_ID(self, FilePath, FileName):

        doc = ET.parse(FilePath+FileName)
        root = doc.getroot()

        MeSH_Unique_ID_list = []

        DescriptorRecord_tag = root.findall("DescriptorRecord")

        for record_cnt in range(0, len(DescriptorRecord_tag)):

            Unique_ID = DescriptorRecord_tag[record_cnt].findtext("DescriptorUI")

            MeSH_Unique_ID_list.append(Unique_ID)

        return MeSH_Unique_ID_list


    # 하나의 descriptorRecord 에 포함되어 있는 모든 이름들을 묶은 것
    def get_All_MeSH_Name_opt(self, FilePath, FileName):

        doc = ET.parse(FilePath+FileName)
        root = doc.getroot()

        MeSH_Name_list = []
        Temp = []

        DescriptorRecord_tag = root.findall("DescriptorRecord")

        for record_cnt in range(0, len(DescriptorRecord_tag)):

            for ai in DescriptorRecord_tag[record_cnt].iter("DescriptorName"):
                Temp.append(str(ai.findtext("String")).lower().strip())

            MeSH_Name_list.append(Temp)

            #초기화 작업
            Temp = []

        return MeSH_Name_list


    # MeSH에서 제공하는 전체 MeSH Name 가지고 옴, 2020년 name 뿐만 아니라 previous MeSH name 포함
    def get_Total_MeSH_Names(self, FilePath, FileName):

        doc = ET.parse(FilePath+FileName)
        root = doc.getroot()

        MeSH_Name_list = []

        for DescriptorName in root.iter("DescriptorName"):
            MeSH_Name_list.append(str(DescriptorName.findtext("String")).lower().strip())

        return MeSH_Name_list


    # MeSH에서 제공하는 전체 ID 가지고 옴, 2020년 name 뿐만 아니라 previous MeSH name의 unique id 포함
    def get_Total_MeSH_Unique_ID(self, FilePath, FileName):

        doc = ET.parse(FilePath+FileName)
        root = doc.getroot()

        MeSH_Unique_ID_list = []

        for Name in root.iter():

            if str(Name.findtext("DescriptorUI")) != str("None"):
                MeSH_Unique_ID_list.append(Name.findtext("DescriptorUI"))


        return MeSH_Unique_ID_list


    # MeSH supplementary data에서 제공하는 전체 MeSH heading에서 해당 되는 name 정보, concept 정보, Term 정보 모두 합쳐서 정리
    # 정보를 합쳐서 name으로 검색하는 경우 name과 관련된 모든 정보를 놓치지 않고 정리하기 위해 사용
    def get_All_MeSH_Concept_Term_Names_supp(self, FilePath, FileName):

        doc = ET.parse(FilePath + FileName)
        root = doc.getroot()

        DescriptorRecord_tag = root.findall("SupplementalRecord")

        MeSH_All_Concept_Term_Name_list = []
        Temp_name = []
        Temp_concept = []
        Temp_term = []

        for record_cnt in range(0, len(DescriptorRecord_tag)):

            for name in DescriptorRecord_tag[record_cnt].iter("SupplementalRecordName"):
                Temp_name.append(str(name.findtext("String")).lower().strip())

            for concept in DescriptorRecord_tag[record_cnt].iter("ConceptName"):
                Temp_concept.append(str(concept.findtext("String")).lower().strip())

            for term in DescriptorRecord_tag[record_cnt].iter("Term"):
                Temp_term.append(str(term.findtext("String")).lower().strip())

            # print("Term list")
            # print(Temp_term)

            Temp = Temp_name + Temp_concept + Temp_term
            # 중복 제거
            Temp = list(set(Temp))

            MeSH_All_Concept_Term_Name_list.append(Temp)

            # 초기화 작업
            Temp_concept = []
            Temp_term = []

        return MeSH_All_Concept_Term_Name_list


    def get_All_MeSH_Unique_ID_supp(self, FilePath, FileName):

        doc = ET.parse(FilePath+FileName)
        root = doc.getroot()

        MeSH_Unique_ID_list = []

        DescriptorRecord_tag = root.findall("SupplementalRecord")

        for record_cnt in range(0, len(DescriptorRecord_tag)):

            Unique_ID = DescriptorRecord_tag[record_cnt].findtext("SupplementalRecordUI")

            MeSH_Unique_ID_list.append(Unique_ID)

        return MeSH_Unique_ID_list
