#!/bin/bash

echo "IFS=${IFS}"

PRE_IFS=$IFS
IFS="
"

gg=$((0))

for i in `ls -al /bin` 
     do
      dd=`echo $i | awk '{print $9 " ===> " $5".KB"}'`
      
      if [ "${$i[0]}" == "." ] || [ "${$i[0]}" == ".." ]; then
          continue
      fi
        
      echo $dd >> $1
      
     done
     echo $dd
IFS=$PRE_IFS

