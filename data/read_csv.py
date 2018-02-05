import pandas as pd
import csv

data = pd.read_csv('orders.csv', sep=',')

# raw_data = []
#
# with open('orders.csv', 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         raw_data.append(row)
#
# data = pd.DataFrame(raw_data[1:], columns=raw_data[0])
#print(data)

data = data[["customer","totalSales"]]
# print(data.count())
# print(data.isnull().sum())
# data = data.dropna()
# print(data.dtypes)
# data[["customer"]] = data[["customer"]].astype(str)
# print(data.dtypes)
# output = data.groupby(["customer"], as_index=False).sum()
# print(output)
#
# customers = []
# sales = []
# for customer in set(data['customer'].tolist()):
#     total_sale = data.loc[data['customer'] == customer, 'totalSales'].sum()
#     customers.append(customer)
#     sales.append(total_sale)
# output = pd.DataFrame({'customer':customers,'total_sale':sales}).sort_values(by='customer')
#
# print(output)
#data['newOrderDate'] = pd.to_datetime(data['orderDate'],infer_datetime_format=True)
print(type(data['customer']))
print(set(data['customer'].values))
