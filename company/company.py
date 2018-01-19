import pandas as pd
import csv

#How many people switched from M to G directly?
#to do:

data = pd.read_csv('company.csv', sep=',')
data['year'] = data['year'].astype(float)
data[['company']] = data[['company']].fillna('')
data[['year']] = data[['year']].fillna('')

print(data.dtypes)
aaa
# raw_data = []
# with open('company.csv', 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         raw_data.append(row)
#
# data = pd.DataFrame(raw_data[1:], columns=raw_data[0])

output = 0
for member in set(data['member_id'].values.tolist()):
    member_data = data.loc[data['member_id'] == member, ['company', 'year']]
    member_data_sort = member_data.sort_values(by = ['year'])
    member_company_sort = member_data_sort['company'].values.tolist()
    if 'M' in member_company_sort:
        m_rank = member_company_sort.index('M')
        if isinstance(m_rank, list) == False:
            m_rank = [m_rank]
    else:
        m_rank = -1
    if 'G' in member_company_sort:
        g_rank = member_company_sort.index('G')
        if isinstance(g_rank, list) == False:
            g_rank = [g_rank]
    else:
        g_rank = -1
    if m_rank != -1 and g_rank != -1:
        for m in m_rank:
            for g in g_rank:
                if g - m == 1:
                    output += 1

print(output)

#How many people switched from M to G ever?
#to do:

data = pd.read_csv('company.csv', sep=',')
data[['year']] = data[['year']].astype(int)
data[['company']] = data[['company']].fillna('')
data[['year']] = data[['year']].fillna('')

# raw_data = []
# with open('company.csv', 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         raw_data.append(row)
#
# data = pd.DataFrame(raw_data[1:], columns=raw_data[0])

output = 0

for member in set(data['member_id'].values.tolist()):
    member_data = data.loc[data['member_id'] == member, ['company', 'year']]
    member_data_sort = member_data.sort_values(by = ['year'])
    member_data_sort.index = range(member_data_sort.shape[0])
    #print(member_data_sort)
    m_rank = member_data_sort.loc[member_data_sort['company'] == 'M', 'company'].index.tolist()
    g_rank = member_data_sort.loc[member_data_sort['company'] == 'G', 'company'].index.tolist()
    #print(m_rank)
    #print(g_rank)
    if m_rank != [] and g_rank != []:
        if min(m_rank) < max(g_rank):
            output += 1
        # for m in m_rank:
        #     for g in g_rank:
        #         if g - m == 1:
        #             output += 1

print(output)

# Count of members per each company
#output = data.groupby('company', as_index=False).member_id.nunique()
output = data.groupby('company')['member_id'].nunique()
print(output)
# print(output.values)
# print(output.index.tolist())
output = pd.DataFrame({'company':output.index.tolist(), 'count':output.values})
#print(output.index.tolist())
#output['company'] = output.index.tolist()
#output.index = range(output.shape[0])
print(output)
