#!/bin/bash

if [ $# -lt 2 ]; then
    echo "두개의 파일명을 입력해주세요.
    "
    exit 0
fi

Date=`date +%Y%m%d --date=yesterday`
fn="${Date}.log"

cat $1 > $fn
cat $2 >> $fn
