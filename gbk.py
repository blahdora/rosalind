from Bio import Entrez
from datetime import datetime

with open("rosalind_gbk.txt", "r") as f:
    lines = f.read().strip().split('\n')

org = lines[0]
start_date = lines[1]
end_date = lines[2]

search_term = f"{org}[Organism]"

Entrez.email = "shalinisinha602@gmail.com"
handle = Entrez.esearch(db="nucleotide", term=search_term, datetype="pdat", mindate=start_date, maxdate=end_date)
record = Entrez.read(handle)
print(record["Count"])
