pwd
ls
dir_name=basename "$PWD"
ssh root@188.166.187.156
[ ! -d /home/dev/temp/$dir_name  ] && mkdir /home/dev/temp/$dir_name || cd /home/dev/temp/$dir_name && rm -rfv ./*
exit
rm -rfv ./.git
find . -name \*.pyc -type f -delete
find . -name \*.*~ -type f -delete
scp -r . root@188.166.187.156:/home/dev/temp/$dir_name
