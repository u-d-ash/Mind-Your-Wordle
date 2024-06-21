from glob_vars import *
from functions import *

class game:

    def __init__(self, answer, hardmode = 0, algo = 0):
        self.solution = answer
        self.hardmode = hardmode
        self.algo = algo
        self.gspace = set(init_guess_space)
        self.sspace = set(init_sol_space)
        self.played_moves = []
    
    def play(self, guess):

        cc = ccomb_to_ind[get_color_comb(guess, self.solution)]

        self.played_moves.append(guess)

        if(self.hardmode):
            self.gspace = get_filter_space(self.gspace, word_to_ind[guess], cc)
        
        self.sspace = get_filter_space(self.sspace, word_to_ind[guess], cc)

        return ind_to_ccomb[cc]

    def simulate(self, start_word):
        
        resp = self.play(start_word)
        moves = 1

        if(resp == "11111"):
            return moves

        while(True):

            if(self.algo == 0):
                opt_moves = max_min_algo(self.gspace, self.sspace)
            elif(self.algo == 1):
                opt_moves = avg_split_algo(self.gspace, self.sspace)

            best_move = opt_moves[0][1][1]
            j = 1
            while(j < len(opt_moves) and best_move in self.played_moves):
                best_move = opt_moves[j][1][1]
                j += 1

            if(len(self.sspace) == 1):
                best_move = ind_to_word[(list)(self.sspace)[0]]

            resp = self.play(best_move)
            moves += 1
            
            if(resp == "11111"):
                return moves

            if(moves > 6):
                return moves
        










