java -Xmx1G -cp $(echo dependency/*jar| tr ' ' ':'):de.tudarmstadt.langtech.semantics.segmentation.topictiling-0.0.1-SNAPSHOT.jar de.tudarmstadt.langtech.lda.LDA $@
