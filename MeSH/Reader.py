import xml.etree.ElementTree as ET

class MeSH_Reader:

    # MeSH에서 제공하는 전체 MeSH의 term 가지고 옴
    def get_All_MeSH_Terms(self, FilePath, FileName):

        doc = ET.parse(FilePath+FileName)
        root = doc.getroot()

        MeSH_Term_list = []
        Temp_term = []

        DescriptorRecord_tag = root.findall("DescriptorRecord")

        for record in range(0, 2): #len(DescriptorRecord_tag)):
            for ai in DescriptorRecord_tag[record].iter('Term'):
                Temp_term.append(ai.findtext('String'))
            MeSH_Term_list.append(Temp_term)

            #초기화 작업 필요, 초기화 진행하지 않으면 데이터가 누적됨
            Temp_term = []

        return MeSH_Term_list


    # MeSH에서 제공하는 전체 MeSH Name 가지고 옴
    def get_All_MeSH_Name(self, FilePath, FileName):

        doc = ET.parse(FilePath+FileName)
        root = doc.getroot()

        MeSH_Name_list = []

        for DescriptorName in root.iter("DescriptorName"):
            MeSH_Name_list.append(DescriptorName.findtext("String"))

        return MeSH_Name_list

    # MeSH에서 제공하는 전체 ID 가지고 옴
    def get_All_MeSH_UniqueID(self, FilePath, FileName):

        doc = ET.parse(FilePath+FileName)
        root = doc.getroot()

        MeSH_Unique_ID_list = []

        for Name in root.iter():

            if str(Name.findtext("DescriptorUI")) != str("None"):
                MeSH_Unique_ID_list.append(Name.findtext("DescriptorUI"))

        return MeSH_Unique_ID_list
