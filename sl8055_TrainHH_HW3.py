#simple version of training stage -- slide 23

# global variables
total = 0

# any word not in this list is OOV (Out of Vocabulary)
all_words = []

Emission = {
        "DT": {},
        "QT": {},
        "CD": {},
        "NN": {},
        "NNS": {},
        "NNP": {},
        "NNPS": {},
        "EX": {},
        "PRP": {},
        "PRP$": {},
        "POS": {},
        "RBS": {},
        "RBR": {},
        "RB": {},
        "JJS": {},
        "JJR": {},
        "JJ": {},
        "MD": {},
        "VB": {},
        "VBP": {},
        "VBZ": {},
        "VBD": {},
        "VBN": {},
        "VBG": {},
        "WDT": {},
        "WP": {},
        "WP$": {},
        "WRB": {},
        "TO": {},
        "IN": {},
        "CC": {},
        "UH": {},
        "RP": {},
        "SYM": {},
        "$": {},
        "\"": {},
        "\\(": {},
        "\\)": {},
        ",": {},
        ".": {},
        ":": {}
        }

Transition = {
        'Begin_Sent': {},
        'End_Sent': {},

        "DT": {},
        "QT": {},
        "CD": {},
        "NN": {},
        "NNS": {},
        "NNP": {},
        "NNPS": {},
        "EX": {},
        "PRP": {},
        "PRP$": {},
        "POS": {},
        "RBS": {},
        "RBR": {},
        "RB": {},
        "JJS": {},
        "JJR": {},
        "JJ": {},
        "MD": {},
        "VB": {},
        "VBP": {},
        "VBZ": {},
        "VBD": {},
        "VBN": {},
        "VBG": {},
        "WDT": {},
        "WP": {},
        "WP$": {},
        "WRB": {},
        "TO": {},
        "IN": {},
        "CC": {},
        "UH": {},
        "RP": {},
        "SYM": {},
        "$": {},
        "\"": {},
        "\\(": {},
        "\\)": {},
        ",": {},
        ".": {},
        ":": {}
        }

def fill_Emission(tr_file):
    with open(tr_file) as f:
        lines = f.readlines()
        #print(lines)
        for l in lines:
            
            if l.strip():
                word, pos = l.strip().split("\t")
                
                if pos not in Emission:
                    Emission[pos] = {}

                if word in Emission[pos]:
                    Emission[pos][word] += 1
                else:
                    Emission[pos][word] = 1
    f.close()

def fill_Transition(tr_file):
    punctuations = [".", "!", "?"]
    # possibly check for :, ; , etc

    sent_ended = False

    # gotta loop again to count Transition
    with open(tr_file) as f:
       #f.seek(0)
        #first_line = f.readline().strip().split("\t")

        lines = f.readlines()
        #print(lines)
        #print(first_line)
    cur = {
        "word": "",
        "pos": ""
        }
    # hardcoding first word
    # Transition['Begin_Sent'][cur["pos"]] = 1

   #  print(cur)

    prev = {
            "word": "",
            "pos": ""
            }
    

    for l in lines:
        
        if l != '\n':  
            cur["word"] = l.strip().split("\t")[0]
            cur["pos"] = l.strip().split("\t")[1]
        
        global total

        if cur["pos"] not in Transition:        
            Transition[cur["pos"]] = {}

        if prev["pos"] in Transition:                
            if prev["word"] in punctuations or total == 0:
                if cur["pos"] in Transition[prev["pos"]]:
                    Transition['Begin_Sent'][cur["pos"]] += 1
                else:
                    # else initialize the inner dictionary
                    Transition['Begin_Sent'][cur["pos"]] = 1
            else:
                if cur["pos"] in Transition[prev["pos"]]:
                    Transition[prev["pos"]][cur["pos"]] += 1
                else:
                    Transition[prev["pos"]][cur["pos"]] = 1
                
            if cur["word"] in punctuations:
                if 'End_Sent' in Transition[cur["pos"]]:
                    Transition[cur["pos"]]['End_Sent'] += 1
                else:
                    Transition[cur["pos"]]['End_Sent'] = 1
        
        
        prev["word"] = cur["word"]
        prev["pos"] = cur["pos"]
        
        
        total += 1
    
'''
    for l in lines:
        if l.strip():
            
            cur["word"] = l.strip().split("\t")[0]
            cur["pos"] = l.strip().split("\t")[1]
            global total
            total += 1
        
        # check for begin_sent and End_Sent
        if sent_ended:
            #Transition["Begin_Sent"][cur["pos"]] = Transition["Begin_Sent"].get(cur["pos"], 0) + 1
            Transition["Begin_Sent"][cur["pos"]] = Transition["Begin_Sent"][cur["pos"]] + 1
            sent_ended = False

        if cur["word"] in punctuations:
            #Transition["End_Sent"][prev["pos"]] = Transition["End_Sent"].get(prev["pos"], 0) + 1
            #Transition["End_Sent"][prev["pos"]] = Transition["End_Sent"].get(prev["pos"], 0) + 1
            Transition["End_Sent"][prev["pos"]] = Transition["End_Sent"][prev["pos"]] + 1
            sent_ended = True


        else:

            if prev["pos"] not in Transition:
                Transition[prev["pos"]] = {}
    
            if cur["pos"] not in Transition[prev["pos"]]:
                Transition[prev["pos"]][cur["pos"]] = 1
            else:
                Transition[prev["pos"]][cur["pos"]] += 1  

        prev["word"] = cur["word"]
        prev["pos"] = cur["pos"]
    #print(Transition)
    #print(total)
    # end of for loop
    f.close()
'''

# loop thru hash table and convert frequencies into probabilities
# freq / total = probability

def calculate_transition_probabilities():
    for prev in Transition:
        for cur in Transition[prev]:
            if Transition[prev][cur] != 0:
                Transition[prev][cur] /= total
    
    #print(Transition)
    return Transition


def calculate_emission_probabilities():
    for pos in Emission:
        for word in Emission[pos]:
            if Emission[pos][word] != 0:
                Emission[pos][word] /= total
    #print(Emission)
    return Emission
#POS -> table of frequencies of words that occur with that POS


def list_words(tr_file):
    for l in tr_file:
        if l.strip():
            word = l.strip().split("\t")[0]
            if word not in all_words:
                all_words.append(word)
    return all_words
    #print(words)

def combine_corpuses(file1, file2):
    with open(file1) as f1:
        for l in f1: 
            if l.strip():
                word = l.strip().split("\t")[0]
                if word not in all_words:
                    all_words.append(word)
    f1.close()
    return all_words


    

