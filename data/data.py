#load packages
import csv
import pandas as pd

#read the orders.csv file
rawData = []
with open("orders.csv","rb") as f:
    reader = csv.reader(f)
    for row in reader:
        rawData.append(row)

data = pd.DataFrame(rawData[1:],columns=rawData[0])
#check NA
print data.notnull()
#filter NA
data = data.dropna()
#or replace NA
data = data.fillna(0)
#check data type
print data.dtypes
#change data type
data[["quantityCount"]] = data[["quantityCount"]].astype(int)
data[["totalSales"]] = data[["totalSales"]].astype(float)
#filter data
data = data[data["totalSales"] >= 500]
data = data[["customer","quantityCount"]]

#case 1: use group_by function
#group by customers
output = data.groupby('customer',as_index=False).sum()
print output

#case 2: do not use group_by function
customers = []
quantityCount = []
for customer in set(data['customer'].values.tolist()):
    customers.append(customer)
    quantityCount.append(sum(data.loc[data['customer'] == customer,"quantityCount"].tolist()))

output = pd.DataFrame({'customer':customers,'quantityCount':quantityCount}).sort_index(by=['customer'])
print output
