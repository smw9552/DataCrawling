
class MeSH_Finder:

    # MeSH name 넣고 id 추출
    def find_MeSH_Diseaes_Name_To_ID(self, Keyword, MeSH_Name_list, MeSH_ID_list):

        Find_Unique_ID = []

        for word in Keyword:

            try:
                Find_Unique_ID.append(MeSH_ID_list[MeSH_Name_list.index(str(word))])

            except ValueError:
                Find_Unique_ID.append(str("None_ID"))

        return Find_Unique_ID







