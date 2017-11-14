import pandas as pd
import csv

data = pd.read_csv('orders.csv', sep=',')

print(data)

# rawData = []
# with open("orders.csv","rb") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         rawData.append(row)
#
# data1 = pd.DataFrame(rawData[1:],columns=rawData[0])
# print(data1)

#data['newOrderDate'] = pd.to_datetime(data['orderDate'],infer_datetime_format=True)

print(data)
