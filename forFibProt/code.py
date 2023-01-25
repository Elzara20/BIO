import sys
import Bio
from Bio import SeqIO
from Bio.Blast import NCBIWWW

import urllib
import os
import re
import glob 

from tqdm import tqdm
import shutil
from joblib import Parallel, delayed
import numpy as np

import requests
import json

from Bio.PDB import *
from Bio.PDB.PDBIO import PDBIO

import csv

import warnings
warnings.filterwarnings('ignore')


print("directory:", os.getcwd())
os.chdir("/home/elzara/pypdb")
print("changed directory:", os.getcwd())

from pypdb.clients.search.search_client import perform_search_with_graph
from pypdb.clients.search.search_client import ReturnType
from pypdb.clients.search.search_client import QueryGroup, LogicalOperator
from pypdb.clients.search.operators import text_operators
from pypdb import *

fib_protein = Query("fibrous | fibrillar").search()
print(f"count of fibrous protein = {len(fib_protein)}")
def download_fasta(fastacode, datadir, downloadurl="https://www.rcsb.org/fasta/entry/"):

    url = downloadurl + fastacode
    outfnm = os.path.join(datadir, fastacode)
    try:
        urllib.request.urlretrieve(url, outfnm)
        return outfnm
    except Exception as err:
        print(str(err), file=sys.stderr)
        return str(err) #None

def only_fasta(i_results):
  if download_fasta(i_results, '/home/elzara/FIB_PROTEIN/fasta/') == 'HTTP Error 404: Not Found':
    print(f'Нет fasta файла для белка {i_results}')
  else:
    download_fasta(i_results, '/home/elzara/FIB_PROTEIN/fasta/')
'''for i in fib_protein:
  print(f"downloading protein {i}...")
  only_fasta(i)
'''
print(len(fib_protein))
#3
path = '/home/elzara/FIB_PROTEIN/fasta/*'
for file in glob.glob(path):
  with open(file, 'r') as pdb_file:
    fasta_file=''
    for record in SeqIO.parse(pdb_file, 'fasta'):
      fasta_file+=record.seq
      
    print(f"making one sequence for {pdb_file.name[31:]} ...")
    with open(f"/home/elzara/FIB_PROTEIN/fasta_one/{pdb_file.name[31:]}_new.fasta", "w") as external_file:  
      print('>' + pdb_file.name[27:], file=external_file)
      print(fasta_file, file=external_file)
    external_file.close()
#3.1

