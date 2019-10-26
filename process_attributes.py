import pandas as pd
import pickle
import numpy as np

def pickle_in(filename):
    with open(filename, 'rb') as pickleFile:
        return pickle.load(pickleFile)

if __name__ == '__main__':
    county_to_idx = pickle_in('county_to_idx')

    n = len(county_to_idx)

    levels_of_education = 4
    education_attributes = {1970:np.zeros((n, levels_of_education)), 1980:np.zeros((n, levels_of_education)),1990:np.zeros((n, levels_of_education)),2000:np.zeros((n, levels_of_education)), 2013:np.zeros((n, levels_of_education))}

    df = pd.read_excel('Education.xls')

    for row in df.iloc[4:].itertuples(index=False):
        county = row[2]+', '+row[1]
        if county in county_to_idx:
            idx = county_to_idx[county]
            for i in range(4):
                education_attributes[1970][idx][i] = row[11+i]
                education_attributes[1980][idx][i] = row[19 + i]
                education_attributes[1990][idx][i] = row[27 + i]
                education_attributes[2000][idx][i] = row[35 + i]
                education_attributes[2013][idx][i] = row[43 + i]

    for year,mat in education_attributes.items():
        np.save('education_'+str(year), mat)


    df = pd.read_excel('Unemployment.xls')
    df = pd.read_excel('PovertyEstimates.xls')
    df = pd.read_excel('PopulationEstimates.xls')
