import json
import pickle

with open("text-data/all_cr.txt") as f:
    c = f.read()

with open("text-data/guesses.txt") as f:
    g = f.read()

with open("text-data/solutions.txt") as f:
    s = f.read()

all_color_combs = c.split("\n")
init_guess_space = g.split("\n")
init_sol_space = s.split("\n")

ind_to_word = {}
ind_to_ccomb = {}
word_to_ind = {}
ccomb_to_ind = {}

for i, cr in enumerate(all_color_combs):
    ccomb_to_ind[cr] = i
    ind_to_ccomb[i] = cr

for i, gw in enumerate(init_guess_space):
    word_to_ind[gw] = i
    ind_to_word[i] = gw

init_guess_space = [word_to_ind[word] for word in init_guess_space]
init_sol_space = [word_to_ind[word] for word in init_sol_space]
all_color_combs = [ccomb_to_ind[cc] for cc in all_color_combs]


with open("precomps/greens.json") as f:
    green_dict = json.load(f)

with open("precomps/greys.json") as f:
    grey_dict = json.load(f)

with open("precomps/posgrey.json") as f:
    posgrey_dict = json.load(f)

with open("precomps/counter.json") as f:
    counter_dict = json.load(f)

with open("precomps/gw_col_matrix.pkl", "rb") as f:

    gw_col_matrix = pickle.load(f)
