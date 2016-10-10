#!/bin/bash
./topictiling.sh -fd "../JGibbLDA/models/speech/topictiling-test-filter/" -fp "speech-00001.txt" -tmd ../JGibbLDA/models/speech/train -tmn model-final -w 3 -out topictiling-result/result
#i=0
#topictiling_test_dir="../src/JGibbLDA/models/speech/topictiling-test/"
#for file in "$topictiling_test_dir"/*
#do
#    let i=i+1
#    printf "%s\n" ${file##*/}
#    out=$(printf "topictiling-result/speech-%05d.txt" $i)
#    ./topictiling.sh -fd $topictiling_test_dir -fp "${file##*/}" -tmd ../JGibbLDA/models/speech/train -tmn model-final -w 2 -out $out
#done
