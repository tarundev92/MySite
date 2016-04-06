#!/bin/bash
cdir=$(basename "$PWD")
echo $cdir
ssh root@188.166.187.156 'bash -s' < script.sh /home/dev/temp/feature/$cdir
rm -rfv ./.git
rm -rfv ./venv
find . -name \*.pyc -type f -delete
find . -name \*.*~ -type f -delete
scp -r . root@188.166.187.156:/home/dev/temp/feature/$cdir
ssh root@188.166.187.156 'bash -s' < script1.sh /home/dev/temp/feature


source /opt/myenv/bin/activate
export PYTHONPATH=/home/tarun/projects/MysiteGitRepo/MySite
export DJANGO_SETTINGS_MODULE=mysite.settings
export HOST_NAME=http://127.0.01/
/home/tarun/projects/MysiteGitRepo/myenv/bin/gunicorn -c /home/tarun/projects/MysiteGitRepo/MySite/scripts/gunicorn.py mysite.wsgi --reload

/home/tarun/projects/MysiteGitRepo/myenv/bin/gunicorn  mysite.wsgi:application -b 127.0.0.1:8000

source /var/www/appzcentre.com/djenv/bin/activate
export PYTHONPATH=/var/www/appzcentre.com/MySite
export DJANGO_SETTINGS_MODULE=mysite.settings
export HOST_NAME=http://45.55.185.30/
python manage.py runserver 45.55.185.30:8000
/var/www/appzcentre.com/djenv/bin/gunicorn -c /var/www/appzcentre.com/MySite/gunicorn.py mysite.wsgi --reload

