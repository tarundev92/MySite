#!/bin/bash
cd $1/MySite/mysite
sed -i 's/'"'"'PASSWORD'"'"''":"' '"'"''"'"''","'/'"'"'PASSWORD'"'"''":"' '"'"''"'"'root'"'"''","'/g' settings.py
exit
