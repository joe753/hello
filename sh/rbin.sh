#!/bin/bash


PRE_IFS=$IFS

IFS="
"

cd /home/dooo
Filename="bin_files.txt"
touch $Filename
aa="="
bb=">"
TOT=0
for i in `ls -al /bin`; do
    S=`echo $i | awk '{print $5}'`
    F=`echo $i | awk '{print $9}'`

    if [ "$F" == "." ] || [ "$F" == ".." ] || [ "$F" == "" ] ; then
        continue
    fi  
   
    
    #TOT=$(( $TOT + $S ))
    TOT=`expr $TOT + $S`
    
    echo "$S $F" >> $Filename
    echo "Downloading =======================>  `expr $TOT + $S`"KB""
 
done

echo "Total Size is $TOT".KB""


IFS=$PRE_IFS
