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
#change data type
data[["quantityCount"]] = data[["quantityCount"]].astype(int)
data[["totalSales"]] = data[["totalSales"]].astype(int)
#filter data
data = data[data["totalSales"] >= 500]
data = data[["customer","quantityCount"]]
#group by customers
output = data.groupby('customer',as_index=False).size()
print output
