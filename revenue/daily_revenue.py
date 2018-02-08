import pandas as pd
from datetime import datetime
import numpy as np

# import data and clean date format
raw_data = pd.read_csv('daily_revenue.csv', sep=',')
#raw_data['date'] = pd.to_datetime(raw_data['date'], infer_date_format = True)
revenue_date = [datetime.strptime(x, '%m/%d/%y') for x in raw_data['date'].values.tolist()]
raw_data['new_date'] = revenue_date

# self join and filter rows
data = pd.merge(raw_data, raw_data, how='inner', on='userid')
data = data.loc[(data['platform_x'] == 'ios') & (data['platform_y'] == 'gpl')]
data = data.loc[(data['new_date_x'] < data['new_date_y'])]
print(data)
print(len(set(data['userid'].values.tolist())))
# print(raw_data)
# raw_data = raw_data.reindex(np.random.permutation(raw_data.index))
# print(raw_data)
