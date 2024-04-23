from glob_vars import *
from functions import *

class game:

    def __init__(self, answer, hardmode = 0):
        self.solution = answer
        self.hardmode = hardmode
        self.gspace = set(init_guess_space)
        self.sspace = set(init_sol_space)
    
    def play(self, guess):

        cc = ccomb_to_ind[get_color_comb(guess, self.solution)]

        if(self.hardmode):
            self.gspace = get_filter_space(self.gspace, word_to_ind[guess], cc)
        
        self.sspace = get_filter_space(self.sspace, word_to_ind[guess], cc)

        return ind_to_ccomb[cc]

    def simulate(self):
        
        # for min-max algo:
        resp = self.play("raise")
        moves = 1

        if(resp == "11111"):
            return moves

        for i in range(5):
            opt_moves = get_optimal_moves(self.gspace, self.sspace)
            best_move = opt_moves[0][1][1]
            resp = self.play(best_move)
            moves += 1
            if(resp == "11111"):
                return moves
        
        return 7

## Hard Mode Min Max Algorithm Sim:

succ_moves = 0
total_moves = 0

for word_ind in tqdm(init_sol_space):

    the_game = game(ind_to_word[word_ind], 1)
    moves = the_game.simulate()
    if(moves <= 6):
        succ_moves += 1
        total_moves += moves

print(f"Success Rate : {round(succ_moves/len(init_sol_space) * 100 , 2)}")
print(f"Avg moves taken in successful games : {round(total_moves/succ_moves, 3)}")








