#!/bin/bash

if [ $# -ne 1 ];then
    echo "Usage: $0 YYYY-MM-DD"
    exit
fi

DATE=$1
echo "TARGET DATE : ${DATE}"
python getstock3.py 1000 9999 ${DATE} &
