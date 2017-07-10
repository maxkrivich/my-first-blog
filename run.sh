#!/bin/bash

if [[ -z $1 ]]; then
  port=8000
else
  port=$1
fi

echo "run server on $port"
find . -name \*.pyc -delete
python manage.py runserver "0:$port"
