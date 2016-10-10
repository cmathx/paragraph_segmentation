paragraph segmentation in topictiling model

File Description:
JGibbLDA
	models
		speech
			topictiling-train - chinese speech with punctuations, one speech per file, one sentence per line
			topictiling-test  - chinese speech with punctuations, one speech per file, one sentence per line
			topictiling-train - chinese speech without punctuations, one speech per file, one sentence per line
			topictiling-test  - chinese speech without punctuations, one speech per file, one sentence per line
			train
				speech_lda.punc.train.txt - train corpus with punctuations for lda modeling
				speech_lda.punc.test.txt  - test corpus with punctuations for lda modeling
				speech_lda.train.txt      - train corpus without punctuations for lda modeling
				speech_lda.test.txt       - test corpus without punctuations for lda modeling
	lda_run.sh - lda modeling script
TopicTiling
	topictiling_run.sh - topictiling modeling scipt
