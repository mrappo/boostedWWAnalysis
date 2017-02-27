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
            
            python MATTEO_runLocal_OneSample_fullCLs.py --mass 1000 --sample Higgs --batchMode
            cd $getBack
        done
