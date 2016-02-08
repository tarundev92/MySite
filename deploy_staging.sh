pwd
ls
dir_name=basename "$PWD"
rm -rfv ./.git
find . -name \*.pyc -type f -delete
find . -name \*.*~ -type f -delete
scp -r . root@188.166.187.156:/home/dev/temp/$dir_name
