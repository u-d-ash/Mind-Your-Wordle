
from glob_vars import *
from tqdm import tqdm
import math

def get_filter_space(space, gw_ind, cc_ind):

    return set(gw_col_matrix[gw_ind][cc_ind]).intersection(space)

def get_optimal_moves(g_space, s_space):

    moves = []

    for gw_ind in g_space:

        min_info = 15

        for cr_ind in all_color_combs:

            ci_len = len(get_filter_space(s_space, gw_ind, cr_ind))

            if(ci_len != 0):
                min_info = min(min_info, -1 * math.log2(ci_len/len(s_space)))
        
        
        moves.append((min_info, (int(gw_ind in s_space), ind_to_word[gw_ind])))
    
    moves.sort(reverse=True)

    return moves

def get_color_comb(guess, ans):

    ans_letter_count = {letter: ans.count(letter) for letter in set(ans)}

    code = ['_'] * 5

    green_inds = []

    for i in range(5):
        if(guess[i] == ans[i]):
            code[i] = '1'
            green_inds.append(i)
            ans_letter_count[guess[i]] -= 1
    
    rem_inds = [i for i in range(5) if i not in green_inds]

    rem_ans_lets = [ans[x] for x in rem_inds]

    greys = []

    for ri in rem_inds:


        if(guess[ri] not in rem_ans_lets):

            code[ri] = '3'
            greys.append(ri)
    

    yell_cands = [i for i in range(5) if i not in greys and i in rem_inds]

    for yi in yell_cands:

        if(ans_letter_count[guess[yi]] >= 1):
            code[yi] = '2'
            ans_letter_count[guess[yi]] -= 1
        else:
            code[yi] = '3'
        
    
    return "".join(code)
    
    



    



