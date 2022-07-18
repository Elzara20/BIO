#!/bin/bash
for file in /home/elzara/content/data_for_blast/*.txt
do
	filename=`basename ${file%%.*}`
	blastp \
		-query $file \
		-db nr \
		-out /home/elzara/results/result_for_blast/res_of_$filename \
		-task blastp-fast \
		-max_target_seqs 3 \
		-num_threads 2
done
