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

def process_education(n):
    levels_of_education = 4
    years = [1970, 1980, 1990, 2000, 2013]
    attributes = {year: np.full((n, levels_of_education), np.nan) for year in years}
    df = pd.read_excel('raw_data/Education.xls')

    for row in df.iloc[4:].itertuples(index=False):
        county = row[2] + ', ' + row[1]
        if county in county_to_idx:
            idx = county_to_idx[county]
            for i in range(4):
                attributes[1970][idx][i] = row[11 + i]
                attributes[1980][idx][i] = row[19 + i]
                attributes[1990][idx][i] = row[27 + i]
                attributes[2000][idx][i] = row[35 + i]
                attributes[2013][idx][i] = row[43 + i]

    for year, mat in attributes.items():
        pickle_out('processed_data/education_' + str(year), mat)

def process_unemployment(n):
    df = pd.read_excel('raw_data/Unemployment.xls')
    years = list(range(2007, 2019))
    attributes = {year: np.full((n, 1), np.nan) for year in years}

    for row in df.loc[6:].itertuples(index=False):
        county = row[2]
        if county in county_to_idx:
            idx = county_to_idx[county]
            for i, year in enumerate(years):
                attributes[year][idx] = row[9 + 4 * i]

    for year, mat in attributes.items():
        pickle_out('processed_data/unemployment_' + str(year), mat)

def process_poverty(n):
    df = pd.read_excel('raw_data/PovertyEstimates.xls')
    attributes = np.full((n, 1), np.nan)

    for row in df.iloc[4:].itertuples(index=False):
        county = row[2] + ', ' + row[1]
        if county in county_to_idx:
            idx = county_to_idx[county]
            attributes[idx] = row[10]

    pickle_out('processed_data/poverty_2017', attributes)

def process_population(n):
    df = pd.read_excel('raw_data/PopulationEstimates.xls')
    years = list(range(2010, 2019))
    attributes = {year: np.full((n, 1), np.nan) for year in years}

    for row in df.iloc[4:].itertuples(index=False):
        county = row[2] + ', ' + row[1]
        if county in county_to_idx:
            idx = county_to_idx[county]
            for i, year in enumerate(years):
                attributes[year][idx] = row[10 + i]

    for year, mat in attributes.items():
        pickle_out('processed_data/population_' + str(year), mat)

if __name__ == '__main__':
    county_to_idx = pickle_in('processed_data/county_to_idx')

    n = len(county_to_idx)

    process_education(n)
    process_unemployment(n)
    process_poverty(n)
    process_population(n)



