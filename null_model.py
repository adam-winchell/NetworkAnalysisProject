from __future__ import absolute_import, division, print_function

import numpy as np
import pickle
import os
import random


class NullModel:
    def __init__(self, feature_matrix):
        self.feature_matrix = feature_matrix
        
    def shuffle(self, n=1000):
        sample_range = list(range(0, len(self.feature_matrix)))
        for i in range(n):
            print('\r%d / %d' % (i, n), end='')
            v1, v2 = random.sample(sample_range, 2)
            tmp = np.copy(self.feature_matrix[v1, 1:])
            self.feature_matrix[v1, 1:] = np.copy(self.feature_matrix[v2, 1:])
            self.feature_matrix[v2, 1:] = tmp

# class NullModel:
#     def __init__(self,adjacency):
#         self.adjacency_matrix = adjacency #adjacency matrix from file
#         self.attributes = [] #unpopulated attributes
#         self.attribute_names = []

#     def populate_attributes(self, path='./data/processed_data'):
#         files = os.listdir(path)
#         for f in files:
#             if '2017' not in f:
#                 continue
#             if f not in ["adj_list","adj_matrix","county_to_idx", 'idx_to_county', 'clean_regression_2017', 'clean_regression_2000', 'clean_regression_1990']: #not an attribute file
#                 with open(path+'/'+f,'rb') as p:
#                     cur_table = pickle.load(p)
#                     if cur_table.shape[1] > 1: #education files have different shape from others
#                         levels = ["noHS", "HSonly", "partialCollege", "completedCollege"] #names for the four different types
#                         for idx, age_range in enumerate(cur_table.swapaxes(1,0)):
#                             name= f + levels[idx]
#                             self.attributes.append(age_range)
#                             self.attribute_names.append(name)
#                     else:
#                         self.attributes.append(cur_table)
#                         self.attribute_names.append(f)

#     #have yet to figure out proper burn in time!
#     def burn_in(self,n=100000,debug=False):
#         for i in range(n):
#             if debug:
#                 print('\r%d / %d' % (i, n), end='')
#             node1, node2 = random.sample(range(0, self.adjacency_matrix.shape[0]), 2)
#             for attr in self.attributes:
#                 attr[node1], attr[node2] = attr[node2], attr[node1]


if __name__ == "__main__":
    data = pickle.load(open('data/processed_data/clean_regression_2017', 'rb'))
    null = NullModel(data)
    null.shuffle(n=1000000)
#     with open('./data/processed_data/adj_matrix','rb') as p:
#         adjacency_matr = pickle.load(p)

#     G = NullModel(adjacency_matr)
#     G.populate_attributes()
#     G.burn_in(debug=True)
