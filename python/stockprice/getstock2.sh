#!/bin/bash

if [ $# -ne 1 ];then
    echo "Usage: $0 YYYY-MM-DD"
    exit
fi

DATE=$1
echo "TARGET DATE : ${DATE}"
python getstock2.py 1000 1999 ${DATE} &
python getstock2.py 2000 2999 ${DATE} &
python getstock2.py 3000 3999 ${DATE} &
python getstock2.py 4000 4999 ${DATE} &
python getstock2.py 5000 5999 ${DATE} &
python getstock2.py 6000 6999 ${DATE} &
python getstock2.py 7000 7999 ${DATE} &
python getstock2.py 8000 8999 ${DATE} &
python getstock2.py 9000 9999 ${DATE} &
