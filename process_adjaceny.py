import numpy as np
from collections import defaultdict
import re
import pickle

def pickle_out(filename, object_to_dump):
    with open(filename, 'wb') as pickleFile:
        pickle.dump(object_to_dump, pickleFile)
        pickleFile.close()

if __name__ == '__main__':
    file = open('raw_data/county_adjacency_raw.txt', 'r', errors='ignore')

    patt = re.compile('\\"(.+)\\"')
    # patt = re.compile('(\d+)')    #if we want to parse by GEOID (which is less susceptible to erros

    current_county = ''
    adj_list = defaultdict(list)
    to_idx = {}
    curr_idx = 0
    for line in file:
        s= re.findall(patt,line)
        if s != []:
            s = s[0].split('"') #comment out if parsing using GEOID

            if len(s) == 3: #change to 2 if using GEOID
                current_county = s[0]

                adj_list[current_county].append(s[2])   #change to s[1] if parsing using GEOID

                if s[2] not in to_idx:  #change to s[1] if parsing using GEOID
                    to_idx[s[2]] = curr_idx #change to s[1] if parsing using GEOID
                    curr_idx += 1
            else:
                adj_list[current_county].append(s[0])

            if s[0] not in to_idx:
                to_idx[s[0]] = curr_idx
                curr_idx += 1


    save_adj_list = {}
    for county, adjs in adj_list.items():
        save_adj_list[to_idx[county]] = [to_idx[c] for c in adjs]

    pickle_out('processed_data/adj_list',save_adj_list)

    n = curr_idx
    adj_matrix = np.zeros((n,n))
    for county, adj_counties in adj_list.items():
        for adj in adj_counties:
            adj_matrix[to_idx[county], to_idx[adj]] = 1

    pickle_out('processed_data/adj_matrix', adj_matrix)

    to_idx = {val:key for key,val in to_idx.items()}
    pickle_out('processed_data/county_to_idx', to_idx)






