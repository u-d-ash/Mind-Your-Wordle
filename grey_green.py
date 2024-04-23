from tqdm import tqdm
import json
from glob_vars import *

# 3 is grey, 2 is yellow, 1 is green

green_dict = {}
posgrey_dict = {}
grey_dict = {}

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

        posgrey_dict[let][j] = list(set(init_guess_space).difference(set(gfil)))

with open("precomps/greens.json", "w") as f:

    json.dump(green_dict, f)

with open("precomps/greys.json", "w") as f:

    json.dump(grey_dict, f)

with open("precomps/posgrey.json", "w") as f:

    json.dump(posgrey_dict, f)













        
