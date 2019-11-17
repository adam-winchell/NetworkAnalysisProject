from __future__ import absolute_import, division, print_function

import numpy as np
import pickle
from sklearn.neighbors import KNeighborsRegressor


def pickle_out(filename, object_to_dump):
    with open(filename, 'wb') as pickleFile:
        pickle.dump(object_to_dump, pickleFile)
        pickleFile.close()


# This isn't used currently, but may be valuable later
def knn_imputation(dataset):
    clf = KNeighborsRegressor(3, weights='distance', n_jobs=-1)
    all_idxs = np.arange(dataset.shape[1])
    valid_rows = np.all(~np.isnan(dataset), axis=1)
    for i in range(dataset.shape[1]):
        nan_idxs = np.where(np.isnan(full_dataset[:, i]))[0]
        if len(nan_idxs) == 0:
            continue
        data_idxs = np.delete(all_idxs, i)
        label_idx = i
        x = dataset[valid_rows]
        x = x[:, data_idxs]
        y = dataset[valid_rows]
        y = y[:, label_idx]
        print(x.shape, y.shape)
        clf_fit = clf.fit(x, y)
        preds_x = dataset[nan_idxs]
        preds_x = preds_x[:, data_idxs]
        imputed_values = clf_fit.predict(preds_x)
        print(imputed_values.shape)


"""
Create 2017 dataset. This dataset contains data from the following:
    * education_2013
    * population_2017
    * poverty_2017
    * unemployment_2017
"""

education = pickle.load(open('processed_data/education_2013', 'rb'))
population = pickle.load(open('processed_data/population_2017', 'rb'))
poverty = pickle.load(open('processed_data/poverty_2017', 'rb'))
unemployment = pickle.load(open('processed_data/unemployment_2017', 'rb'))
idxs = np.arange(0, len(education))[:, np.newaxis]

full_dataset = np.concatenate((idxs, education, population, poverty, unemployment), axis=1)
print('2017 raw full data shape:', full_dataset.shape)
print('Number of nans:', np.count_nonzero(np.isnan(full_dataset)))
valid_rows = np.all(~np.isnan(full_dataset), axis=1)
full_dataset = full_dataset[valid_rows]
print('2017 clean full dataset shape:', full_dataset.shape)
pickle_out('processed_data/clean_regression_2017', full_dataset)


"""
Create 2000 dataset. This dataset contains data from the following:
    * education_2000
    * population_1999
    * poverty_1999
"""

education = pickle.load(open('processed_data/education_2000', 'rb'))
population = pickle.load(open('processed_data/population_1999', 'rb'))
poverty = pickle.load(open('processed_data/poverty_1999', 'rb'))
idxs = np.arange(0, len(education))[:, np.newaxis]

full_dataset = np.concatenate((idxs, education, population, poverty), axis=1)
print('\n2000 raw full data shape:', full_dataset.shape)
print('Number of nans:', np.count_nonzero(np.isnan(full_dataset)))
valid_rows = np.all(~np.isnan(full_dataset), axis=1)
full_dataset = full_dataset[valid_rows]
print('2000 clean full dataset shape:', full_dataset.shape)
pickle_out('processed_data/clean_regression_2000', full_dataset)

"""
Create 1990 dataset. This dataset contains data from the following:
    * education_1990
    * population_1989
    * poverty_1989
"""

education = pickle.load(open('processed_data/education_1990', 'rb'))
population = pickle.load(open('processed_data/population_1989', 'rb'))
poverty = pickle.load(open('processed_data/poverty_1989', 'rb'))
idxs = np.arange(0, len(education))[:, np.newaxis]

full_dataset = np.concatenate((idxs, education, population, poverty), axis=1)
print('\n1990 raw full data shape:', full_dataset.shape)
print('Number of nans:', np.count_nonzero(np.isnan(full_dataset)))
valid_rows = np.all(~np.isnan(full_dataset), axis=1)
print(np.sum(valid_rows))
full_dataset = full_dataset[valid_rows]
print('1990 clean full dataset shape:', full_dataset.shape)
pickle_out('processed_data/clean_regression_1990', full_dataset)
