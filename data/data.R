#load packages
library(dplyr)


#read the orders.csv
rawData <- read.csv("orders.csv",header=T)

#change data types
rawData$quantityCount <- as.numeric(rawData$quantityCount)
rawData$totalSales <- as.numeric(rawData$totalSales)
#filter data
data <- filter(rawData,totalSales >= 500)
data <- select(data,customer,quantityCount)
#group by customers
byCustomers <- group_by(data,customer)
output <- summarise(byCustomers,totalQuantity = sum(quantityCount))
output
