import csv
import re
import glob


find_protein_after_domains=[]

for file in glob.glob("/home/elzara/FIB_PROTEIN/InterPro/tsv_result/*_new.tsv.tsv"):
  with open(file) as protein:
    # print(f"protein = {protein}")
    tsv_file = csv.reader(protein, delimiter="\t")
    for line in tsv_file:
      # print(f"line of tsv file:\n{line}")
      #if (line[3] == "Pfam"):
      #print(f"prot = {line[0]}")
      #print(f"name = {line[5]}")
      find_word = re.findall('([Ff]ibr[a-z]+)|([Ff]iber)|([Cc]ollagen)|([Kk]eratin)|([Ee]lastin)', line[5])
      if len(find_word)!=0:
        print(f"{line[0][4:]}")
        print(f"find pattern = {find_word}")
        print(f"name = {line[5]}")
        find_protein_after_domains.append(line[0][4:])

print("FIBROUS PROTEINS")
print(find_protein_after_domains)
print(f"count of fib_protein = {len(find_protein_after_domains)}")

