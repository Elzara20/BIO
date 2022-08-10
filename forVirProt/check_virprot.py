from Bio.PDB import PDBParser
from Bio.PDB import PDBIO

from pypdb.clients.search.search_client import perform_search_with_graph
from pypdb.clients.search.search_client import ReturnType
from pypdb.clients.search.search_client import QueryGroup, LogicalOperator
from pypdb.clients.search.operators import text_operators
from pypdb import *

import sys
import Bio
from Bio import SeqIO
from Bio.Blast import NCBIWWW

import urllib
import os
import re
import glob # для файлов в папке

from tqdm import tqdm
import shutil
from joblib import Parallel, delayed
import numpy as np

import requests
import json

from Bio.PDB import *
from Bio.PDB.PDBIO import PDBIO

def del_fasta(entity, FASTAFile): # формируем фаста файл из нужных сущностей
  with open(f"/content/V_PROTEINS/newfasta/new{FASTAFile[-4:]}.fasta", "w") as external_file:
    with open(FASTAFile, 'r') as fasta_file:
      for record in SeqIO.parse(fasta_file, 'fasta'):
        # print(record.id)
        for i in entity:
          if i in record.id:
            print('>' + record.id, file=external_file)
            print(record.seq, file=external_file)
  external_file.close()

# del_fasta(['4YC2_2', '4YC2_3'], '/content/V_PROTEINS/fasta/4YC2')

def del_pdb(chains, PDBFile): # удаляем ненужное
  parser = PDBParser()
  print(PDBFile)
  structure = parser.get_structure("",f"{PDBFile}")
  for model in structure:
    for i in range(len(chains)): #=='B' or chain.id=='H' or chain.id=='C' or chain.id=='L'):
      model.detach_child(chains[i])
        
  print(f'counter={counter}')
  w = PDBIO()
  w.set_structure(structure)
  w.save(f'/content/V_PROTEINS/newpdb/new{PDBFile[-8:]}')
# del_pdb(['2', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'n'], '/content/V_PROTEINS/pdb/7SYP.pdb')

def chain_formation(chains):  
  res=re.findall('[A-Za-z0-9]', str(chains))
  return res

API_KEY = '86bda4dcbf604e13e46df647f88b71fa3e09'
db='taxonomy'
path = '/content/V_PROTEINS/pdb/*'
for file in glob.glob(path):
  chains_for_del=[]
  entity_for_del=[]

  pdb_file = get_pdb_file(file[-8:-4], filetype='pdb', compression=False)
  id_taxonomy_keys=re.findall('ORGANISM_TAXID: ([0-9]+);', str(pdb_file))
  chain=re.findall('CHAIN: ([A-Z,a-z,0-9, ,]+,*);', str(pdb_file))
  for number, id in enumerate(id_taxonomy_keys):
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db={db}&id={id}&api_key={API_KEY}'
    res = requests.get(url)
    taxseq=re.findall('<Lineage>(.+)</Lineage>', str(res.text))
    find_word=re.findall('virus[a-z]*|viri[a-z]+', str(taxseq))
    counter=0
    if len(find_word)==0:
      print(f'NOT VIRUS: {file[-8:-4]}_{number+1}')
      
      chains_for_del.append(chain[number])
    else:
      entity_for_del.append(f'{file[-8:-4]}_{number+1}')

  
  if len(entity_for_del)!=0:
    print(f'chains_for_del ==== {chains_for_del}')
    print(f'entity_for_del ==== {entity_for_del}')
    del_pdb(chain_formation(chains_for_del), file)
    del_fasta(entity_for_del, f'/content/V_PROTEINS/fasta/{file[-8:-4]}')
