#load packages
library(dplyr)


#read the orders.csv
rawData <- read.csv("orders.csv",header=T)

#change data types
rawData$quantityCount <- as.numeric(rawData$quantityCount)
rawData$totalSales <- as.numeric(rawData$totalSales)

#case 1: use 'dplyr' package
#filter data
data <- filter(rawData,totalSales >= 500)
data <- select(data,customer,quantityCount)
#group by customers
byCustomers <- group_by(data,customer)
output <- summarise(byCustomers,totalQuantity = sum(quantityCount))
output

#case 2: do not use 'dplyr' package
data <- rawData[rawData$totalSales > 500,]
data <- data[c("customer","quantityCount")]
#calculate via a loop
uniqueCustomers = as.character(unique(data$customer))
customers = rep(0,length(uniqueCustomers))
quantityCounts = rep(0,length(uniqueCustomers))
for (i in 1:length(uniqueCustomers)){
  customer = uniqueCustomers[i]
  print(customer)
  customerQuantity = data[data$customer == customer,]
  customers[i] <- customer
  print(customers)
  quantityCounts[i] <- sum(customerQuantity$quantityCount)
}
output <- data.frame(customer = customers,quantityCount = quantityCounts)
output

#order the output if necessary
output[with(output,order(-totalQuantity)),]
#or
arrange(output,desc(totalQuantity))
