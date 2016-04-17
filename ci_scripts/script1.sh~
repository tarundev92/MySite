#!/bin/bash
tar -xvzf $1$2.tar.gz -C $1
rm $1$2.tar.gz
sed -i 's/'"'"'PASSWORD'"'"''":"' '"'"''"'"''","'/'"'"'PASSWORD'"'"''":"' '"'"'root'"'"''","'/g' $1$2/mysite/settings.py
#sed -i 's/'"'"'USER'"'"''":"' '"'"'root'"'"''","'/'"'"'USER'"'"''":"' '"'"'root'"'"''","'/g' $1$2/mysite/settings.py
sudo pkill gunicorn
rm -rf $1$3
mv $1$2 $1$3
cd $1$3
source /var/www/djenv/bin/activate
export PYTHONPATH=/var/www/MySite
export DJANGO_SETTINGS_MODULE=mysite.settings
export HOST_NAME=http://128.199.185.127/
python manage.py makemigrations
python manage.py migrate
nohup /var/www/djenv/bin/gunicorn -c /var/www/MySite/scripts/gunicorn.py mysite.wsgi --reload > /dev/null 2>&1&
exit
