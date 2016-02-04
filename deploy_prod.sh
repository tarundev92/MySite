ssh dev@188.166.187.156
TextN00k
sudo bash
TextN00k

source env/bin/activate

cd mysite
git clone https://github.com/tarundev92/MySite.git
cd MySite

cd mysite
sed -i 's/'"'"'PASSWORD'"'"''":"' '"'"''"'"''","'/'"'"'PASSWORD'"'"''":"' '"'"'root'"'"''","'/g' settings.py

cd ..

python manage.py makemigrations
python manage.py migrate
python manage.py test polls


