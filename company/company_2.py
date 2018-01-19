import pandas as pd
import csv

#How many people switched from M to G ever?
#to do:

data = pd.read_csv('company.csv', sep=',')
data['year'] = data['year'].astype(int)
data[['company']] = data[['company']].fillna('')
data = data.dropna()

# print(data.loc[data['company'] == 'M', 'member_id'])

data = pd.merge(data, data, on='member_id', how='inner', suffixes=['_a','_b'])
#print(data.dtypes)
output = data.loc[(data['company_a'] == 'M') & (data['company_b'] == 'G') & (data['year_a'] < data['year_b']), 'member_id']

print(output.values)

#How many people switched from M to G directly?
#to do:

data = pd.read_csv('company.csv', sep=',')
data['year'] = data['year'].astype(int)
data[['company']] = data[['company']].fillna('')
data = data.dropna()

# print(data.loc[data['company'] == 'M', 'member_id'])
data = data.sort_values(by=['member_id', 'year'], ascending=[True, False])
data['rnk'] = data.index
print(data)

data = pd.merge(data, data, on='member_id', how='inner', suffixes=['_a','_b'])

output = data.loc[(data['company_a'] == 'M') & (data['company_b'] == 'G') & (data['year_a'] - data['year_b'] == -1), 'member_id']

print(len(set(output.values)))

output = data.loc[(data['company_a'] == 'M') & (data['company_b'] == 'G') & (data['rnk_a'] - data['rnk_b'] == -1), 'member_id']
print(len(set(output.values)))
