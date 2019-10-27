import pandas as pd
import pickle
import numpy as np


def pickle_out(filename, object_to_dump):
    with open(filename, 'wb') as pickleFile:
        pickle.dump(object_to_dump, pickleFile)
        pickleFile.close()

def pickle_in(filename):
    with open(filename, 'rb') as pickleFile:
        return pickle.load(pickleFile)

if __name__ == '__main__':
    county_to_idx = pickle_in('processed_data/county_to_idx')

    n = len(county_to_idx)

    levels_of_education = 4
    years = [1970,1980,1990,2000,2013]
    attributes = {year: np.full((n,levels_of_education),np.nan) for year in years}
    df = pd.read_excel('raw_data/Education.xls')

    for row in df.iloc[4:].itertuples(index=False):
        county = row[2]+', '+row[1]
        if county in county_to_idx:
            idx = county_to_idx[county]
            for i in range(4):
                attributes[1970][idx][i] = row[11+i]
                attributes[1980][idx][i] = row[19 + i]
                attributes[1990][idx][i] = row[27 + i]
                attributes[2000][idx][i] = row[35 + i]
                attributes[2013][idx][i] = row[43 + i]

    for year,mat in attributes.items():
        pickle_out('education_'+str(year), mat)


    df = pd.read_excel('raw_data/Unemployment.xls')
    years = list(range(2007,2019))
    attributes = {year:np.full((n,1),np.nan) for year in years}

    for row in df.loc[6:].itertuples(index=False):
        county = row[2]
        if county in county_to_idx:
            idx = county_to_idx[county]
            for i, year in enumerate(years):
                attributes[year][idx] = row[9+4*i]

    for year, mat in attributes.items():
        pickle_out('unemployment_'+str(year), mat)

    # df = pd.read_excel('raw_data/PovertyEstimates.xls')
    # df = pd.read_excel('raw_data/PopulationEstimates.xls')