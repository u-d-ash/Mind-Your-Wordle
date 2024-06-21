from tqdm import tqdm
import json
from glob_vars import *

# 3 is grey, 2 is yellow, 1 is green

green_dict = {}
posgrey_dict = {}
grey_dict = {}
counter_dict = {}

for i in tqdm(range(26)):

    let = chr(i + 97)

    fil_g = []

    for gw in init_guess_space:

        if(let not in ind_to_word[gw]):

            fil_g.append(gw)
    
    grey_dict[let] = fil_g

for i in tqdm(range(26)):

    let = chr(i + 97)

    green_dict[let] = {}
    posgrey_dict[let] = {}

    for j in range(5):

        gfil = []
        
        for gw in init_guess_space:

            if(ind_to_word[gw][j] == let):
                gfil.append(gw)
            
        green_dict[let][j] = gfil

for i in tqdm(range(26)):
        
    let = chr(i + 97)

    posgrey_dict[let] = {}

    hasword = set()

    for k in range(5):
        hasword = hasword.union(green_dict[let][k])
    
    for j in range(5):

        posgrey_dict[let][j] = list(hasword.difference(set(green_dict[let][j])))

for gw in tqdm(init_guess_space):

    word = ind_to_word[gw] 

    for let in set(word):

        if(let in counter_dict.keys()):

            if(word.count(let) in counter_dict[let].keys()):
                counter_dict[let][word.count(let)].append(gw)
            else:
                counter_dict[let][word.count(let)] = [gw]
        else:
            counter_dict[let] = {}
            counter_dict[let][word.count(let)] = [gw]

with open("precomps/greens.json", "w") as f:

    json.dump(green_dict, f)

with open("precomps/greys.json", "w") as f:

    json.dump(grey_dict, f)

with open("precomps/posgrey.json", "w") as f:

    json.dump(posgrey_dict, f)

with open("precomps/counter.json", "w") as f:

    json.dump(counter_dict, f)













        
