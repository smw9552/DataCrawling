class Data_Writer:

    def write_disease_to_id_file_txt(self, OutputFilePath, OutputFileName, Input_Name_list, MeSH_Unique_ID_list):

        Final_data_string = "Disease Name" + "\t" + "MeSH_Unique_ID" + "\n"

        f = open(OutputFilePath+OutputFileName, 'w')

        for ai in range(0, len(Input_Name_list)):

            Final_data_string = Final_data_string + str(Input_Name_list[ai]) + "\t" + str(MeSH_Unique_ID_list[ai]) + "\n"


        f.write(Final_data_string)
        f.close()

        print("Write file")

"""
    def write_disease_to_All_id_file_txt(self, OutputFilePath, OutputFileName, Input_Name_list, MeSH_Unique_ID_list, MeSH_xml_total_Unique_ID_list):

        Final_data_string = "Disease Name" + "\t" + "MeSH_Unique_ID" + "\t" + "MeSH_All_Unique_ID" + "\n"

        f = open(OutputFilePath+OutputFileName, 'w')

        for ai in range(0, len(Input_Name_list)):

            Final_data_string = Final_data_string + str(Input_Name_list[ai]) + "\t" + str(MeSH_Unique_ID_list[ai]) + "\t" + str(MeSH_xml_total_Unique_ID_list[ai]) + "\n"

        f.write(Final_data_string)
        f.close()

        print("Write file")
"""