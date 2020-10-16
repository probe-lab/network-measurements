#!/bin/bash

i="0"
while [ $i -lt 15 ] 
do 
if [ $(fuser /var/lib/dpkg/lock) ]; then 
  i="0" 
fi 
sleep 1 
i=$[$i+1] 
done
