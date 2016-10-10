The programme can be executed from commandline (using the topictiling.sh script) and outputs the text and the suggested boundaries. The parameters of the script are shown when just executing the shell script:
 [java] Option "-fd" is required
 [java] java -jar myprogram.jar [options...] arguments...
 [java]  -dn      : Use the direct neighbor otherwise the highest neighbor will be used
 [java]             (default false)
 [java]  -fd VAL  : Directory fo the test files
 [java]  -fp VAL  : File pattern for the test files
 [java]  -i N     : Number of inference iterations used to annotate words with topic
 [java]             IDs (default 100)
 [java]  -m       : Use mode counting (true/false) (default=true)
 [java]  -out VAL : File the content is written to (otherwise stdout will be used)
 [java]  -ri N    : Use the repeated inference method
 [java]  -rs N    : Use the repeated segmentation
 [java]  -tmd VAL : Directory of the topic model (GibbsLDA should be used)
 [java]  -tmn VAL : Name of the topic model (GibbsLDA should be used)
 [java]  -w N     : Window size used to calculate the sentence similarity


The parameters -fp, -fd, -tmd, -tmn are the ones that have to be specified and –ri should be parametrized by using about 5 repeated inferences.
For the algorithms it’s important to have a trained LDA model. The model should be in a similar domain as the data you apply my algorithm. You have to train it yourself using GibssLda++ or JGibbslda (http://gibbslda.sourceforge.net/) . They both have the same output format. The output of my algorithms is in xml format:
<document>
<documentName>…</documentName>
<segment>
<depthScore>score<depthScore>
<text>…</text>
</segment>
…

</document>
The code returns all maxima where a boundary might be set. If the number of segments should be given use the N highest depthScore values.
