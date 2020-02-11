import xml.etree.ElementTree as ET

class MeSH_Reader:

    def get_All_MeSH_Name(self, FilePath, FileName):

        doc = ET.parse(FilePath+FileName)
        root = doc.getroot()

        MeSH_Name_list = []

        for DescriptorName in root.iter("DescriptorName"):
            MeSH_Name_list.append(DescriptorName.findtext("String"))

        return MeSH_Name_list


    def get_All_MeSH_UniqueID(self, FilePath, FileName):

        doc = ET.parse(FilePath+FileName)
        root = doc.getroot()

        MeSH_Unique_ID_list = []

        for Name in root.iter():

            if str(Name.findtext("DescriptorUI")) != str("None"):
                MeSH_Unique_ID_list.append(Name.findtext("DescriptorUI"))

        return MeSH_Unique_ID_list
