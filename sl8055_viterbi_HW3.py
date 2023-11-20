import train as ts
import numpy as np
import os
from collections import defaultdict

# use the training corpus to create the tables

def generate_transducer_chart(sentence, TRANSITION_PROBS, EMISSION_PROBS):
    result = []
    #sentence = ['The', 'man', 'runs', '.']

    #num_words = len(words)
    num_tags = len(EMISSION_PROBS.keys()) + 2 # +2 for start and end symbols
    pos_list = list(EMISSION_PROBS.keys())

    rows = num_tags
    cols = len(sentence)

    chart = [[0 for i in range(cols)] for j in range(rows)]

    # structure:
    # predicted_pos = { word : pos }
    # problem: dictionary is overriting words if the owrd is already in a sentence.
    # use a list of tuples.
    predicted_pos = []
    #predicted_pos = {}

    percentage = 0
    # filling in Begin_Sent -> first word probabilities.
    # columns - each word
    # rows - all possible POS
    # the for loop fills in the first column of the chart, which is the first word's probability of being each of the POS
    pos_assigned = False

    
    temp_predicted_pos = "" # dict! because mutable and flexible as of now.

    for i in range(len(chart)-2):
        
        if sentence[0] in EMISSION_PROBS[pos_list[i]] and pos_list[i] in TRANSITION_PROBS['Begin_Sent']:
            print('brah')
            new_percentage = TRANSITION_PROBS['Begin_Sent'][pos_list[i]] * EMISSION_PROBS[pos_list[i]][sentence[0]]
            chart[i][0] = new_percentage
            # choose the most likely POS of the first word.
            if new_percentage > percentage:
                #predicted_pos[sentence[0]] = pos_list[i]
                #predicted_pos[sentence[0]].append(pos_list[i])
                #predicted_pos.append((sentence[0], pos_list[i]))
                temp_predicted_pos = pos_list[i]
                pos_assigned = True

            percentage = max(percentage, new_percentage)

    if not pos_assigned:
        #oov word
        predicted_pos.append((sentence[0], 'NNP'))
    else:
        predicted_pos.append((sentence[0], temp_predicted_pos))

    #prev_pos = predicted_pos[sentence[0]]
    
    # reset percentage to avoid conflict with next for loop
    percentage = 0
    # now, fill out the rest of the chart, column by column.
    # essentially.. the probability = Transitions[prev_pos][cur_pos] * Emissions[pos][sentences[col_num]]
    
    for col_num in range(1, len(chart[0])):
        # reset row number every time you go to next column
        row_num = 0
        # reset percentage every time you go to next column (word)
        percentage = 0
        # update prev_pos to the POS of prev word.
        # prev_pos = predicted_pos[sentence[col_num - 1]]
        prev_pos = predicted_pos[0][1]
        pos_assigned = False
        temp_predicted_pos = ""
        for i in range(len(pos_list)):
            new_percentage = 0
            cur_pos = pos_list[i]
            
            
            if sentence[col_num] in EMISSION_PROBS[cur_pos] and cur_pos in TRANSITION_PROBS[prev_pos]: # if they are not true, probabilty is 0 anyway
                new_percentage = TRANSITION_PROBS[prev_pos][cur_pos] * EMISSION_PROBS[cur_pos][sentence[col_num]]
                chart[row_num][col_num] = new_percentage
                # choose the most likely POS
            if new_percentage > percentage:
                #predicted_pos[sentence[col_num]] = cur_pos
                #predicted_pos[sentence[col_num]].append(cur_pos)
                #predicted_pos.append((sentence[col_num], cur_pos))
                temp_predicted_pos = cur_pos
                pos_assigned = True
            percentage = max(percentage, new_percentage)

            row_num += 1

        if not pos_assigned:
            #predicted_pos[sentence[col_num]].append('JJ')
            predicted_pos.append((sentence[col_num], 'JJ'))
        else:
            predicted_pos.append((sentence[col_num], temp_predicted_pos))

    print(predicted_pos)
    return predicted_pos
    #generate_output_file(predicted_pos)




        