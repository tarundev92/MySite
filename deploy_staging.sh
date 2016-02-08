pwd
ls
dir_name=basename "$PWD"
ssh root@188.166.187.156
if [ ! -d /home/dev/temp/$dir_name  ] 
then
   mkdir /home/dev/temp/$dir_name
else
cd /home/dev/temp/$dir_name
rm -rfv ./*
fi
exit
rm -rfv ./.git
find . -name \*.pyc -type f -delete
find . -name \*.*~ -type f -delete
scp -r . root@188.166.187.156:/home/dev/temp/$dir_name
