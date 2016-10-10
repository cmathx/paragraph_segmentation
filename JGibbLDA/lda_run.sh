#!/bin/bash

nohup java -mx512M -cp bin:lib/args4j-2.0.6.jar jgibblda.LDA -est -alpha 0.5 -beta 0.01 -ntopics 300 -niters 100 -savestep 100 -twords 50 -dir models/speech/train/ -dfile speech_lda.train.txt > init_model_run.log 2>&1 &
nohup java -mx512M -cp bin:lib/args4j-2.0.6.jar jgibblda.LDA -estc -dir models/speech/train/ -model model-final -ntopics 300 -niters 400 -savestep 100 -twords 50 > iter_model_run.log 2>&1 &
nohup java -mx512M -cp bin:lib/args4j-2.0.6.jar jgibblda.LDA -inf -dir models/speech/train -model model-final -niters 100 -twords 50 -dfile speech_lda.test.txt > test_run.log 2>&1 &
