# Viterbi-HMM-POS-tagger

# This program takes in the WSJ_23.words corpus, which is a corpus consisting of words only.
It produces an output file called submission.pos which predicts the part-of-speech of every word in WSJ_23.words.

<b>The Hidden Markov Model (HMM) in sl8055_trainHH_HW3.py is trained based on the Training file and Development file.</b>
- Transition table: contains probability of every part-of-speech tag and the part-of-speech tag that comes after.
- Emission table: contains probability of every word and its part-of-speech tag.
- Both tables are stored as dictionaries.
  
<b>The viterbi algorithm in sl8055_viterbi_HW3.py takes the Transition and Emission tables and calculates the part-of-speech tag of each word in WSJ_23.words.</b>

Assignment for CSCIUA-480 Natural Language Processing

<br>
<br>

Training file (WSJ_02-21.pos): ~950K words, ~40k sentences
<br>
Development file (WSJ_24.pos): ~32.9K words, ~1350 sentences
<br>
Development test file (WSJ_24.words): the same as WSJ_24.pos, but without the POS tags
<br>
Test file (WSJ_23.words): ~56.7K words, ~2415 sentences
<br>
These words all come from the Wall Street Journal.

