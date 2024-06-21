from tqdm import tqdm
from glob_vars import *
import pickle

gwcol_matrix = [[[] for _ in range(len(all_color_combs))] for _ in range((len(init_guess_space)))]

def assign_filter_space(i, j):
        
    comp_resp = get_color_response(i, j)

    greens = comp_resp[0]
    posgreys = comp_resp[1]
    greys = comp_resp[2]
    count_conts = comp_resp[3]

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
    
    for cc in count_conts:

        let = cc[0]
        counter = cc[1]

        space = space.intersection(set(counter_dict[let][chr(counter + 48)]))


    for aword in space:
        gwcol_matrix[i][j].append(aword)


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

    count_conds = []

    for g in greys:

        if(g not in g_lets and g not in yells):

            final_greys.append(g)
        
        elif(g in g_lets or g in yells):

            totka = 0

            for x in g_lets:

                totka += (x == g)
            
            for x in yells:

                totka += (x == g)
            
            count_conds.append([g, totka])

    
    return (set(greens), set(posgreys), set(final_greys), count_conds)

for i in tqdm(range(len(init_guess_space))):

    for j in range(len(all_color_combs)):

        assign_filter_space(i, j)

with open('precomps/gw_col_matrix.pkl', 'wb') as f:
    pickle.dump(gwcol_matrix, f)

