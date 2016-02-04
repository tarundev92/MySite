sudo bash
TextN00k
source env/bin/activate
cd MySiteRepo
git clone https://github.com/tarundev92/MySite.git
cd MySite
cd mysite
sed -i 's/'"'"'PASSWORD'"'"''":"' '"'"''"'"''","'/'"'"'PASSWORD'"'"''":"' '"'"'root'"'"''","'/g' settings.py
cd ..
python manage.py makemigrations
python manage.py migrate
python manage.py test polls
