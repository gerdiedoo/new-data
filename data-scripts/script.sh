#!/bin/bash  
  
#file name
file='links.txt'  
#directory name
dir='hash-map'
mkdir $dir
i=1  

while read line; do
    # output contains carriage return that needs to be removed, need to truncate
    str=$(echo "$line" | tr -d '\r')
    end=${line##*/}
    col=$((${#line} - ${#end}))
    temp="$str $i-${line:col}"
    # echo "$temp"
    git clone $temp
    mv $i-${line:col} $dir
    i=$((i+1))  
    
done < $file  
