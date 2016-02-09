#!/bin/bash
if [ ! -d $1  ]
then
 mkdir $1 
else
 rm -rfv $1/*
fi
exit
