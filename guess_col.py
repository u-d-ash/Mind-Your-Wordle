from tqdm import tqdm
from glob_vars import *
import pickle

gwcol_matrix = [[[] for _ in range(len(all_color_combs))] for _ in range((len(init_guess_space)))]

def assign_filter_space(i, j):
        
    comp_resp = get_color_response(i, j)

    greens = comp_resp[0]
    posgreys = comp_resp[1]
    yells = comp_resp[2]
    greys = comp_resp[3]

    space = set(init_guess_space)
    
    for g in greens:

        let = g[0]
        ind = g[1]

        space = space.intersection(set(green_dict[let][chr(ind + 48)]))
    
    for g in greys:

        space = space.intersection(set(grey_dict[g]))

    for g in posgreys:

        let = g[0]
        ind = g[1]

        space = space.intersection(set(posgrey_dict[let][chr(ind + 48)]))


    newspace = []

    for word_ind in space:
    
        match = True
        word_letter_counts = {letter: ind_to_word[word_ind].count(letter) for letter in set(ind_to_word[word_ind])}
        guess_letter_counts = {letter: "".join(yells).count(letter) for letter in set(yells)}
        
        for k in guess_letter_counts.keys():

            if(k not in word_letter_counts.keys()):
                match = False
                break
            else:
                if(guess_letter_counts[k] > word_letter_counts[k]):
                    match = False
                    break

        
        if(match):
            gwcol_matrix[i][j].append(word_ind)
            #newspace.append(ind_to_word[word_ind])
        
    #return newspace

def get_color_response(word_ind, seq_ind):

    greens = []
    g_lets = []
    greys = []
    yells = []
    final_greys = []
    posgreys = []

    word = ind_to_word[word_ind]
    seq = ind_to_ccomb[seq_ind]

    for i in range(5):

        if(seq[i] == '1'):

            greens.append((word[i], i))
            g_lets.append(word[i])

        elif(seq[i] == '3'):

            greys.append(word[i])
        
        elif(seq[i] == '2'):

            posgreys.append((word[i], i))
            yells.append(word[i])


    for g in greys:

        if(g not in g_lets and g not in yells):

            final_greys.append(g)
    
    return (set(greens), set(posgreys), yells, set(final_greys))

for i in tqdm(range(len(init_guess_space))):

    for j in range(len(all_color_combs)):

        assign_filter_space(i, j)

with open('precomps/gw_col_matrix.pkl', 'wb') as f:
    pickle.dump(gwcol_matrix, f)

