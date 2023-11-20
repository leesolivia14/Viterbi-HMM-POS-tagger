# Viterbi-HMM-POS-tagger

This program takes in the WSJ_23.words corpus, which is a corpus consisting of words only.
It produces an output file called submission.pos which predicts the part-of-speech of every word in WSJ_23.words.

The Hidden Markov Model (HMM) in sl8055_trainHH_HW3.py is trained based on the Training file and Development file.
- Transition table: contains probability of every part-of-speech tag and the part-of-speech tag that comes after.
- Emission table: contains probability of every word and its part-of-speech tag.
- Both tables are stored as dictionaries.
  
The viterbi algorithm in sl8055_viterbi_HW3.py takes the Transition and Emission tables and calculates the part-of-speech tag of each word in WSJ_23.words.

Assignment for CSCIUA-480 Natural Language Processing



Training file (WSJ_02-21.pos): ~950K words, ~40k sentences

Development file (WSJ_24.pos): ~32.9K words, ~1350 sentences

Development test file (WSJ_24.words): the same as WSJ_24.pos, but without the POS tags

Test file (WSJ_23.words): ~56.7K words, ~2415 sentences

These words all come from the Wall Street Journal.

