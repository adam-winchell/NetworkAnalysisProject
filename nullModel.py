from __future__ import absolute_import, division, print_function

import numpy as np
import pickle
import os
import random

class nullModel:

	def __init__(self,adjacency):
		self.adjacency_matrix = adjacency #adjacency matrix from file
		self.attributes = [] #unpopulated attributes
		self.attribute_names = []

	def populate_attributes(self,path='./processed_data'):
		files = os.listdir(path)
		for f in files:
			if f not in ["adj_list","adj_matrix","county_to_idx"]: #not an attribute file
				with open(path+'/'+f,'rb') as p:
					cur_table = pickle.load(p)
					if cur_table.shape[1] > 1: #education files have different shape from others
						levels = ["noHS", "HSonly", "partialCollege", "completedCollege"] #names for the four different types
						for idx,age_range in enumerate(cur_table.swapaxes(1,0)):
							name=f+levels[idx]
							self.attributes.append(age_range)
							self.attribute_names.append(name)
						pass
					else:
						self.attributes.append(cur_table)
						self.attribute_names.append(f)

	#have yet to figure out proper burn in time!
	def burn_in(self,n=100000,debug=False):
		for i in range(n):
			if debug:
				print('\r%d / %d' % (i,n),end='')
			node1,node2 = random.sample(range(0,self.adjacency_matrix.shape[0]),2)
			for attr in self.attributes:
				attr[node1],attr[node2] = attr[node2],attr[node1]





if __name__ == "__main__":

	with open('./processed_data/adj_matrix','rb') as p:
		adjacency_matr = pickle.load(p)

	G = nullModel(adjacency_matr)
	G.populate_attributes()
	G.burn_in(debug=True)






