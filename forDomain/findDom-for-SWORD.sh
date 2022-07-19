#!/bin/bash
for file in /home/elzara/pdb/*
do
	filename=`basename ${file%%.*}`
	./SWORD -i $file -v > full-domains-of-$filename-SWORD.tab
	grep -n 'ASSIGNMENT' full-domains-of-$filename-SWORD.tab | grep -o "[0-9]*" > \
		start-$filename.txt
	grep -n 'ALTERNATIVES' full-domains-of-$filename-SWORD.tab | grep -o "[0-9]*" > \
		end-$filename.txt
	len_start=$(awk 'END{print NR}' start-$filename.txt)
	len_end=$(awk 'END{print NR}' end-$filename.txt)
#	echo $len_start, $len_end
	if [[ $len_start -ne $len_end ]]
	then
		echo "$(awk 'END{print NR}' full-domains-of-$filename-SWORD.tab)" >> end-$filename.txt
	fi

	
	
	paste -d@ start-$filename.txt end-$filename.txt | while IFS="@" read -r s1 e1
	do
	awk -v s=$(($s1+1)) -v e=$(($e1-1)) 'NR==s,NR==e' full-domains-of-$filename-SWORD.tab | \
		awk -F"|" '{print $3}' | \
		grep "[0-9]*\-[0-9]*" | \
		awk '{print $1}' >> domains-interval-$filename-SWORD.tab

	done
done

