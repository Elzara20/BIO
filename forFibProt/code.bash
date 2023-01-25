#!/bin/bash
i=1
waitevery=30

for j in $(find `pwd` -type f -name "*_new.fasta")
do
   # echo "Iteration: $i; File: $j"
    filename=`basename ${j%%.*}`
    

    echo $filename
    echo $i
    python3 /home/elzara/webservice-clients/python/iprscan5.py \
        --goterms \
        --pathways \
        --email=e.mazinova@g.nsu.ru \
        --outfile=/home/elzara/FIB_PROTEIN/InterPro/tsv_result/${filename} \
        --outformat=tsv \
        --quiet \
        $j & (( i++%waitevery==0 )) && wait
done
