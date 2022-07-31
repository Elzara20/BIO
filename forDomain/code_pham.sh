#!/bin/bash
for file in /home/elzara/Globular/fasta_one/*
do
	#echo file=$file
	filename=`basename ${file%%.*}`
	echo filename=$filename
	filelink=$(echo "'<$file'")
	#echo filelink=$filelink
	curl -LH 'Expect:' -F seq="<$file" -F output=xml 'https://pfam.xfam.org/search/sequence' > res_$filename.xml
	link1=$(grep '<result_url>' res_$filename.xml)
	#echo link1=$link1
	link2=$(echo $link1 | cut -c 13- | rev | cut -c14- | rev)
	#echo link2=$link2
	link3=$(echo https://pfam.xfam.org$link2)
	#echo link3=$link3
	sleep 1m
	wget -O $filename.pfam.txt "$link3"
	sed -i -E 's/<location start=\"([0-9]*)\" end=\"([0-9]*)\"(.*)/START=\1 END=\2/' $filename.pfam.txt
	grep 'START' $filename.pfam.txt > dom_$filename.txt
	#findseq=$(find . -regextype sed -regex "<location start=\"[0-9]+\" end=\"[0-9]+\"")
	#echo findseq=$findseq
done

