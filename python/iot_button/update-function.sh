#!/bin/bash

aws lambda update-function-code \
--region ap-northeast-1 \
--function-name iot_button \
--zip-file fileb://package.zip
