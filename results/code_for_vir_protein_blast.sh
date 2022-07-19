#!/bin/bash
for file in /home/elzara/content/data_for_blast/*.txt
do
	filename=`basename ${file%%.*}`
	blastp \
		-query $file \
		-db nr \
		-out /home/elzara/results/res_of_$filename \
		-task blastp-fast \
		-max_target_seqs 5 \
		-num_threads 10
done
