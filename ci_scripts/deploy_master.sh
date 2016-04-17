#!/bin/bash
mys=$(basename "$PWD")
mys1=$(basename "$PWD")"1"
echo $mys
rm -rfv ./.git
rm -rfv ./venv
find . -name \*.pyc -type f -delete
find . -name \*.*~ -type f -delete
cd ..
mv $mys $mys1
tar -zcvf $mys1.tar.gz $mys1
#cd $mys1
#ssh root@128.199.185.127 'bash -s' < ci_scripts/script.sh /var/www/$tnb1
#cd ..
scp $mys1.tar.gz root@128.199.185.127:/var/www
cd $mys1
ssh root@128.199.185.127 'bash -s' < ci_scripts/script1.sh /var/www/ $mys1 MySite
exit
