#!/bin/bash

aws lambda create-function \
--region ap-northeast-1 \
--function-name iot_button \
--zip-file fileb://package.zip \
--role arn:aws:iam::${AWS_ACCOUNT_ID}:role/iot_button-dev  \
--handler app.post_to_slack \
--runtime python3.6 \
--timeout 15 \
--memory-size 512
