pwd
ls
dir_name = basename "$PWD"
rm -rfv ./.git
rm -rfv ./venv
find . -name \*.pyc -type f -delete
find . -name \*.*~ -type f -delete
basename "$PWD"
scp -r . root@188.166.187.156:/home/dev/temp/basename "$PWD"
