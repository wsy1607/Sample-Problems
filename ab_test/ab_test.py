#this script is bootstrapping for ab testing statistical analysis

#import pagkages
import os, time, sys, json, csv, random
import pandas as pd
import numpy as np


#run the query
group_a = pd.read_csv('group_a.csv', sep=',')
group_b = pd.read_csv('group_b.csv', sep=',')


group_a = group_a['DAY30_GOLD'].values.tolist()
group_b = group_b['DAY30_GOLD'].values.tolist()

n = 100000
results = 0
for i in range(n):
    sample_a = [random.choice(group_a) for _ in group_a]
    sample_b = [random.choice(group_b) for _ in group_b]
    mean_a = np.mean(sample_a)
    mean_b = np.mean(sample_b)
    #print(mean_a)
    #print(mean_b)
    if mean_a < mean_b:
        results += 1

print(float(results)/n)

aaa

data = data.reindex(np.random.permutation(data.index))
data1 = pd.DataFrame(columns=['GAME_USER_ID', 'SEGMENT_ID'])
data2 = pd.DataFrame(columns=['GAME_USER_ID', 'SEGMENT_ID'])
data3 = pd.DataFrame(columns=['GAME_USER_ID', 'SEGMENT_ID'])
for segment_id in set(data['SEGMENT_ID'].values):
    segment = data.loc[data['SEGMENT_ID'] == segment_id, ['GAME_USER_ID', 'SEGMENT_ID']]
    n = segment.shape[0]
    k = int(n/3)
    data1 = pd.concat([data1, segment.iloc[0:k]])
    data2 = pd.concat([data2, segment.iloc[k:2*k]])
    data3 = pd.concat([data3, segment.iloc[2*k:3*k]])


# data1 = data.iloc[0:2000]
# data2 = data.iloc[2000:4000]
# data3 = data.iloc[4000:6000]

data1.to_csv('data1.csv', index=False)
data2.to_csv('data2.csv', index=False)
data3.to_csv('data3.csv', index=False)
