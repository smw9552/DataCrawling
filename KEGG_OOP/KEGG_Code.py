from urllib.request import urlopen
from urllib.error import HTTPError
import socket

class KEGG_Code:

   """
   *KEGG API code list
    full name = code
    pathway = path
    brite = br
    module = md
    orthology = ko
    genome = gn
    gene = vg
    compound = cpd
    glycan = gl
    reation = rn
    rlcass = rc
    enzyme = ec
    network = ne
    variant = has_var
    disease = ds
    drug = dr
    dgroup = dg
    environ = ev
   """

   def getAll_KO_Entry(Self):

       KO_List = []

       KO_URL = "http://rest.kegg.jp/list/ko"

       try:
           KO_Info = urlopen(KO_URL, None, timeout=100000)

           while True:
               KO_line = KO_Info.readline()
               if not KO_line: break

               Temp_KO_line = str(KO_line[:9]).replace("b'ko:","").replace("'","")

               KO_List.append(Temp_KO_line)

       except HTTPError as e:
           print("HTTPError")
           print(e)

       except TimeoutError as e:
           print("Timeout Error")
           print(e)

       except socket.timeout:
           print("Timeout")

       except Exception as e:
           print(e)

       return KO_List

   def getAll_Disease_Entry(self):

       Disease_List = []

       DISEASE_URL = "http://rest.kegg.jp/list/ds"

       try:
           DISEASE_Info = urlopen(DISEASE_URL, None, timeout = 100000)

           while True:
               DISEASE_line = DISEASE_Info.readline()
               if not DISEASE_line: break

               Temp_DISEASE_line = str(DISEASE_line[:9]).replace("b'ds:","").replace("'","")

               Disease_List.append(Temp_DISEASE_line)

       except HTTPError as e:
           print("HTTPError")
           print(e)

       except TimeoutError as e:
           print("Timeout Error")
           print(e)

       except socket.timeout:
           print("Timeout")

       except Exception as e:
           print(e)

       return Disease_List


   def getAll_Pathway_Entry(self):

       Pathway_List = []

       PATHWAY_URL = "http://rest.kegg.jp/list/pathway"

       try:
           PATHWAY_Info = urlopen(PATHWAY_URL, None, timeout = 100000)

           while True:
               PATHWAY_line = PATHWAY_Info.readline()
               if not PATHWAY_line: break

               Temp_PATHWAY_line = str(PATHWAY_line[:13]).replace("b'path:","").replace("'","")

               Pathway_List.append(Temp_PATHWAY_line)

       except HTTPError as e:
           print("HTTPError")
           print(e)

       except TimeoutError as e:
           print("Timeout Error")
           print(e)

       except socket.timeout:
           print("Timeout")

       except Exception as e:
           print(e)

       return Pathway_List

   def getAll_EC_Protein_Entry(self):

       Protein_List = []

       PROTEIN_URL = "http://rest.kegg.jp/list/ec"

       try:
           PROTEIN_Info = urlopen(PROTEIN_URL, None, timeout = 100000)

           while True:
               PROTEIN_line = PROTEIN_Info.readline()
               if not PROTEIN_line: break

               Temp_PROTEIN_line = str(PROTEIN_line[:10]).replace("b'ec:","").replace("'","")

               #print(Temp_PROTEIN_line)

               Protein_List.append(Temp_PROTEIN_line)

       except HTTPError as e:
           print("HTTPError")
           print(e)

       except TimeoutError as e:
           print("Timeout Error")
           print(e)

       except socket.timeout:
           print("Timeout")

       except Exception as e:
           print(e)

       return Protein_List

   def getAll_Metabolite_Entry(self):

       Metabolite_List = []

       METABOLITE_URL = "http://rest.kegg.jp/list/cpd"

       try:
           PROTEIN_Info = urlopen(METABOLITE_URL, None, timeout = 100000)

           while True:
               PROTEIN_line = PROTEIN_Info.readline()
               if not PROTEIN_line: break

               Temp_PROTEIN_line = str(PROTEIN_line[:10]).replace("b'cpd:","").replace("'","")

               #print(Temp_PROTEIN_line)

               Metabolite_List.append(Temp_PROTEIN_line)

       except HTTPError as e:
           print("HTTPError")
           print(e)

       except TimeoutError as e:
           print("Timeout Error")
           print(e)

       except socket.timeout:
           print("Timeout")

       except Exception as e:
           print(e)

       return Metabolite_List


   def getAll_Reaction_Entry(self):

       Reaction_List = []

       REACTION_URL = "http://rest.kegg.jp/list/rn"

       try:
           PROTEIN_Info = urlopen(REACTION_URL, None, timeout = 100000)

           while True:
               PROTEIN_line = PROTEIN_Info.readline()
               if not PROTEIN_line: break

               Temp_PROTEIN_line = str(PROTEIN_line[:10]).replace("b'rn:","").replace("'","").replace("\\t","")

               #print(Temp_PROTEIN_line)

               Reaction_List.append(Temp_PROTEIN_line)

       except HTTPError as e:
           print("HTTPError")
           print(e)

       except TimeoutError as e:
           print("Timeout Error")
           print(e)

       except socket.timeout:
           print("Timeout")

       except Exception as e:
           print(e)

       return Reaction_List


   def getAll_Cell_line_Entry(self):

        Cell_line_List = []

        CELL_LINE_URL = 'http://rest.kegg.jp/list/cell'

        try:
            Cell_line_Info = urlopen(CELL_LINE_URL, None, timeout=1000000)

            while True:
                Cell_line_line = Cell_line_Info.readline()
                if not Cell_line_line: break

                Cell_line_List.append(str(Cell_line_line[0:16]).replace("b'cell:","").replace("'",""))


        except HTTPError as e:
            print(e)
        except TimeoutError as e:
            print(e)
        except socket.timeout:
            print('timeout')
        except Exception as e:
            print(e)

        return Cell_line_List


   def getAll_Gene_target_Entry(self):

        Gene_target_List = []

        GENE_TARGET_URL = "http://rest.kegg.jp/list/genome"

        try:
            Gene_target_Info = urlopen(GENE_TARGET_URL, None, timeout=1000000)

            while True:
                Gene_target_line = Gene_target_Info.readline()
                if not Gene_target_line: break

                Gene_target_List.append(str(Gene_target_line[0:9]).replace("b'gn:",""))

        except HTTPError as e:
            print(e)
        except TimeoutError as e:
            print(e)
        except socket.timeout:
            print('timeout')
        except Exception as e:
            print(e)

        return Gene_target_List

   def getAll_Species_Entry(self):

       Species_List = []

       SPECIES_URL = "http://rest.kegg.jp/list/organism"

       try:
           Species_Info = urlopen(SPECIES_URL, None, timeout=1000000)

           while True:
               Species_line = Species_Info.readline()
               if not Species_line: break

               Species_List.append(str(Species_line[0:6]).replace("b'","").replace("'",""))
               #print(str(Species_line[0:6]).replace("b'","").replace("'",""))

       except HTTPError as e:
           print(e)
       except TimeoutError as e:
           print(e)
       except socket.timeout:
           print('timeout')
       except Exception as e:
           print(e)

       return Species_List




