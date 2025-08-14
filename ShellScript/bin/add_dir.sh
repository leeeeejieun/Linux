#!/bin/bash

BASEDIR=/test
mkdir -p $BASEDIR && cd $BASEDIR && rm -rf $BASEDIR/*

for i in {1..5} 
do
    mkdir -p $i
    for j in {1..5}
    do
        mkdir -p $BASEDIR/$i/$j
    done
done