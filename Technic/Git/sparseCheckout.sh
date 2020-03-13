#!/bin/bash

if [ $# -ge 3 ]
then
    git init $1
    cd $1

    git config core.sparseCheckout true
    git remote add -f origin $2

    args=("$@")
    i=3
    while [ $i -le $# ]
    do
        echo ${args[$i-1]} >> .git/info/sparse-checkout
        i=$(($i+1))
    done

    git pull origin master
else
    echo "Need to more than 3 Arguments"
    echo "1: Diretory Name to Make, 2. Remote Git URL, 3. SubDirectory Names"
fi