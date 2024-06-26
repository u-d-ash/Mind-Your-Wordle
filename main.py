from glob_vars import *
from functions import *

def play_game():

    gspace = set(init_guess_space)
    sspace = set(init_sol_space)

    while(True):

        x = input()
        word = x.split()[0]
        seq = x.split()[1]

        # Uncomment this for hard mode :
        # gspace = get_filter_space(gspace, word_to_ind[word], ccomb_to_ind[seq]) 
        sspace = get_filter_space(sspace, word_to_ind[word], ccomb_to_ind[seq])

        print([ind_to_word[x] for x in sspace])

        if(len(sspace) == 1):
            print(f"The answer is : {ind_to_word[(list)(sspace)[0]]}")
            break
        
        moves = max_min_algo(gspace, sspace)

        for j in range(min(5, len(moves))):

            print(f"{moves[j][1][1]} | ({round(moves[j][0], 7)})")


play_game()
    


