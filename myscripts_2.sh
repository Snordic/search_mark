#!/bin/bash

#Скирп для bitbake ARM по всем конфигам
list=$(ls 'defconfig/')
for i in $list
do
    ./for_defconfig.py defconfig/$i new_config/$i $i
done