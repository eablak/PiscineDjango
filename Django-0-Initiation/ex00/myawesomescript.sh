#!/bin/bash 

if [ -z "$1" ]
then
    echo "Error: URL eksik!"
    exit 1
fi

curl -s $1 | grep "body" |cut -d'"' -f2