#data = {"Header": {"UserID": "ABC", "RawData": {"Transaction": {"Date": "2015-03-03", "Amount": 20.00, "Description": "Burger King"}}}}
data11 = {"a11":1}
data1 = {"a1":data11,"a2":2}
data3 = {"c1":3,"c2":4}
data = {"a":data1,"b":2,"c":data3}

def getkeys(data):
    keys = []
    for key in data.keys():
        keys.append(key)
    return(keys)

def recu(dictKeys,data):
    dictKeys += getkeys(data)
    for key in data.keys():
        if type(data[key]) is dict:
            dictKeys = recu(dictKeys,data[key])
    #print dictKeys
    return(dictKeys)

output = recu([],data)
#get unique keys
output = list(set(output))
print output
