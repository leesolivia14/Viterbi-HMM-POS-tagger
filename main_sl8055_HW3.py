import train as ts
import viterbi as vt
import os

''' run the system 

writing use the training corpus to create the tables and run the system on the development corpus.
For the final system, merge the training and development and run on the test.
'''

def create_output_file():
    if not os.path.exists("submission.pos"):
        f = open("submission.pos", "x")
 
def generate_output_file(predicted_pos):
    
   with open("submission.pos", "a") as f:
       # rememember, predicted_pos is a list of tuples
        for word in predicted_pos:
           f.write(word[0] + "\t" + word[1] + "\n")
        f.write("\n")
       # for word in predicted_pos:
           # f.write(word + "\t" + predicted_pos[word] + "\n")
        #f.write("\n")
    



if __name__ == '__main__':

    training_corpus = "WSJ_02-21.pos"
    dev_corpus = "WSJ_24.pos"
    ALL_WORDS = ts.list_words(training_corpus)


    ts.fill_Transition(training_corpus)
    ts.fill_Transition(dev_corpus)
    TRANSITION_PROBS = ts.calculate_transition_probabilities()

    ts.fill_Emission(training_corpus)
    ts.fill_Emission(dev_corpus)
    EMISSION_PROBS = ts.calculate_emission_probabilities()

    DEV_WORDS = []

    DEV_SENTENCES = []
    #dev_test_file = "WSJ_24.words"
    test_file = "WSJ_23.words"

    dev_sentence = []
    with open(test_file) as f:
        lines = f.readlines()
        for word in lines:
            DEV_WORDS.append(word.strip())
            if word.strip() != '':
                dev_sentence.append(word.strip())
            if word == '\n':
                DEV_SENTENCES.append(dev_sentence)
                dev_sentence = []


    #print(DEV_WORDS)
    create_output_file()

    for sentence in DEV_SENTENCES:
        predicted_pos = vt.generate_transducer_chart(sentence, TRANSITION_PROBS, EMISSION_PROBS)
        generate_output_file(predicted_pos)
    #print(transducer_chart)

    #vt.viterbi(dev_file)
    
    

