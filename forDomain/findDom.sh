#!/bin/bash
for file in /home/elzara/fasta/*
do
	set -u
	hmmscan --domtblout $file-found-domains.tab Pfam-A.hmm $file
	found_domains=$file-found-domains.tab
	cat $found_domains | grep -v "^#" | \
		sed 's/  */\t/g' | cut -f 20,21 > $file-domains-interval.txt
done
	
