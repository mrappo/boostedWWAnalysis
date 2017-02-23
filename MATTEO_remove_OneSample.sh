#!/bin/bash

counter=0
file="DirectoryForFullCLs.txt"
while IFS= read -r line
do
        # display $line or do somthing with $line
	printf '%f\n' "$counter"
	printf '%s\n' "$line"
	DirVector[$counter]=$line
	echo ${DirVector[$counter]}
	((counter++))
	
done <"$file"

#echo ${DirVector[5]}


getBack='../../../../../../../../../'
#cd ${DirVector[5]}

#pwd


#cd $getBack
#ls
#pwd

for i in `seq 0 $((counter-1))`; do
            printf '\n'
            echo item: $i
            cd ${DirVector[$i]}
            pwd
            
            rm -r higgsCombineBulkGraviton600.HybridNew.mH600.*
            #python MATTEO_runLocal_OneSample_fullCLs.py --batchMode
            cd $getBack
        done
