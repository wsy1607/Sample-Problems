data = {"Header": {"UserID": "ABC", "RawData": {"Transaction": {"Date": "2015-03-03", "Amount": 20.00, "Description": "Burger King"}}}}

def getkeys(data):
    for key in data.keys():
        print key

def recu(data):
    getkeys(data)
    for key in data.keys():
        if type(data[key]) is dict:
            recu(data[key])

recu(data)
