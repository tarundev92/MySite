#!/bin/bash
cdir=$(basename "$PWD")
echo $cdir
ssh root@188.166.187.156 /home/dev/temp/script.sh $cdir
rm -rfv ./.git
find . -name \*.pyc -type f -delete
find . -name \*.*~ -type f -delete
scp -r . root@188.166.187.156:/home/dev/temp/$cdir
