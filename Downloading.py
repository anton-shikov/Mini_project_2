from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq

Entrez.email, Entrez.tool = '271296251017a@gmal.com', 'MyCustomScript'

handle = Entrez.efetch(db='nucleotide', id='KF848938.1', rettype= 'fasta', retmode='txt')
record = SeqIO.read(handle, 'fasta')
print(record)
SeqIO.write(record, r'{o}'.format(o=input()), 'fasta')
