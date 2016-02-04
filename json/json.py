data = {"Header": {"UserID": "ABC", "RawData": {"Transaction": {"Date": "2015-03-03", "Amount": 20.00, "Description": "Burger King"}}}}


def getkeys(data):
    keys = []
    for key in data.keys():
        keys.append(key)
    return(keys)

def recu(dictKeys,data):
    dictKeys += getkeys(data)
    for key in data.keys():
        if type(data[key]) is dict:
            recu(dictKeys,data[key])
    return(dictKeys)

output = recu([],data)
print output
