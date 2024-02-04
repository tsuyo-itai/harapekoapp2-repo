#!/bin/bash

# 存在するzipの削除
[ -e ./lambda_function.zip ] && rm lambda_function.zip
[ -e ./lambda_function ] && rm -r lambda_function

# ライブラリ群の作成
if [ ! -e ./lib ]; then
    pip3 install -t ./lib -r ../src/fastapiapp/requirements.txt
fi

# ライブラリ群のZip化
cd lib
zip ../lambda_function.zip -r .

# srcのZip化
cd ..
cd ../src/fastapiapp
zip -u ../../infra/lambda_function.zip main.py
zip -u ../../infra/lambda_function.zip database.py
zip -ur ../../infra/lambda_function.zip schemas
zip -ur ../../infra/lambda_function.zip routers
zip -ur ../../infra/lambda_function.zip cert

# S3へアップロード (第1引数にバケットが設定されている場合)
if [ -n "$1" ]; then
    echo upload to s3 $1
    cd ../../infra
    aws configure list > /dev/null 2>&1

    # aws configure list の終了コードを確認
    if [ $? -eq 0 ]; then
        # S3バケットの存在を確認
        aws s3api head-bucket --bucket $1 2>/dev/null
        # バケットが存在しない場合は作成
        if [ $? -ne 0 ]; then
            aws s3 mb s3://$1 
            echo create s3 bucket $1
        fi
        # S3バケットへのアップロード
        aws s3 cp lambda_function.zip s3://$1/
    fi
fi