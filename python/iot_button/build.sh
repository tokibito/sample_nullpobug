#!/bin/bash

if [ -e package.zip ]
then
  rm package.zip
fi

if [ -e tmp ]
then
  rm -r tmp/*
fi

mkdir -p tmp
cp app.py tmp/
pip install -r requirements.txt -t tmp
pushd tmp/
zip -r ../package.zip ./*
popd
