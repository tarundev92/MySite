#!/bin/bash
cdir=$(basename "$PWD")
echo $cdir
ssh root@188.166.187.156 'bash -s' < script.sh /home/dev/temp/$cdir
rm -rfv ./.git
rm -rfv ./venv
find . -name \*.pyc -type f -delete
find . -name \*.*~ -type f -delete
scp -r . root@188.166.187.156:/home/dev/temp/$cdir
ssh root@188.166.187.156 'bash -s' < script1.sh /home/dev/temp
#testing 
