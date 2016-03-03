#Author: Shengying Wang
#I have completed all three functions, parse(), summarize() and recommend()
#When calling those functions, it prints out the results as expected
#I also wrote vissum() for summarizing data visually
#I am not using the class framework, so I leave the class method as blank
#I am using random forest to predict the recommended coffee
#Given a person's rating records, train the data by cross validation to find the
#best random forest parameters, then predict ratings for all coffees and recommend
#three coffees with highest predicted ratings
#The recommend() function will take up to a few minutes to run
#Thank you!

from __future__ import print_function
import argparse
import re
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

COUNTRIES = {
    "Balinese": "Bali",
    "Bolivian": "Bolivia",
    "Brazilian": "Brazil",
    "Costa Rican": "Costa Rican",
    "Dominican": "Dominican Republic",
    "Salvadorean": "El Salvador",
    "Ethiopian": "Ethiopia",
    "Guatemalan": "Guatemala",
    "Indian": "India",
    "Kenyan": "Kenya",
    "Malian": "Mali",
    "Mexican": "Mexico",
    "Panamanian": "Panama",
    "Peruvian": "Peru",
    "Sumatran": "Sumatra",
}


class Coffee(object):
    @classmethod
    def fromname(cls, name):
        # to be implemented
        raise NotImplementedError


def parse(name):
    features = {}
    booleanFeatures = ["Decaf","Organic","Fair Trade"]
    for booleanFeature in booleanFeatures:
        if booleanFeature in name:
            features[booleanFeature] = True
            name = name.replace(booleanFeature,"")
        else:
            features[booleanFeature] = False
    for country in COUNTRIES.keys():
        if country in name:
            features["Country"] = COUNTRIES[country]
            name = name.replace(country,"")
    features["Adjective"] = name.strip()
    for feature in features.keys():
        print(feature + "      " + str(features[feature]))
    return features


def summarize(file):
    personIdList = []
    ratingList = []
    coffeeNameList = []
    #get personId, rating and coffee name by splitting each line
    for line in file:
        line = line.strip("\n")
        personIdList.append(re.split(r'\t+',line)[0])
        ratingList.append(re.split(r'\t+',line)[2])
        coffeeNameList.append(re.split(r'\t+',line)[1])
    #get features by parse() function
    decafList = []
    organicList = []
    fairTradeList = []
    adjectiveList = []
    countryList = []
    for name in coffeeNameList:
        features = parse(name)
        decafList.append(features["Decaf"])
        organicList.append(features["Organic"])
        fairTradeList.append(features["Fair Trade"])
        adjectiveList.append(features["Adjective"])
        countryList.append(features["Country"])
    #Start printing the summarized statistics
    #print total people
    print("Total people    " + str(len(set(personIdList))))
    #print unique coffee
    print("Total coffee types    " + str(len(set(coffeeNameList))))
    #print decaf info
    print("Decaf")
    print("\tTrue " + str(decafList.count(True)))
    print("\tFalse " + str(decafList.count(False)))
    #print organic info
    print("Organic")
    print("\tTrue " + str(organicList.count(True)))
    print("\tFalse " + str(organicList.count(False)))
    #print fair trade info
    print("Fair Trade")
    print("\tTrue " + str(fairTradeList.count(True)))
    print("\tFalse " + str(fairTradeList.count(False)))
    #print adjective info
    print("Adjective")
    for adjective in set(adjectiveList):
        print(adjective + " " + str(adjectiveList.count(adjective)))
    #print country info
    print("Country")
    for country in set(countryList):
        print(country + " " + str(countryList.count(country)))
    #visualize the summary
    vissum(decafList,organicList,fairTradeList,adjectiveList,countryList)
    #return as a dataframe
    data = {}
    data["personId"] = personIdList
    data["decaf"] = decafList
    data["organic"] = organicList
    data["fairTrade"] = fairTradeList
    data["adjective"] = adjectiveList
    data["country"] = countryList
    data["rating"] = ratingList
    data["coffeeName"] = coffeeNameList
    data = pd.DataFrame(data)
    return(data)

def recommend(file):
    data = summarize(file)
    #change data type
    data[["coffeeName"]] = data[["coffeeName"]].astype(str)
    data[["adjective"]] = data[["adjective"]].astype(str)
    data[["country"]] = data[["country"]].astype(str)
    data[["personId"]] = data[["personId"]].astype(int)
    data[["rating"]] = data[["rating"]].astype(int)
    data[["decaf"]] = data[["decaf"]].astype(int)
    data[["fairTrade"]] = data[["fairTrade"]].astype(int)
    data[["organic"]] = data[["organic"]].astype(int)
    #get training data as all rating records
    trainingData = data.copy()
    #get testing data as all unique coffee types
    testingData = data.copy()
    testingData = testingData.drop("personId",axis=1)
    testingData = testingData.drop("rating",axis=1)
    testingData = testingData.drop_duplicates()
    #define column names
    XColumns = ["adjective","country","decaf","fairTrade","organic"]
    dummyColumns = ["adjective","country"]
    YColumn = ["rating"]
    #work on recommendations for each person
    #collect personId, coffee name and predicted rating as output
    personIdList = []
    coffeeNameList = []
    predictedRatingList = []
    for personId in set(trainingData["personId"].values.tolist()):
        #model is trained for each person using her/his own ratings
        #after training the data, we consider all coffees for prediction
        #the 3 coffee with highest predicted rating will be recommended per person
        personData = data.loc[trainingData["personId"]==personId]
        #if one person rate the same coffee multiple times, get the average
        personData = personData.groupby(XColumns+["coffeeName"],as_index=False).mean()
        #check if this person has enough records
        if personData.shape[0] < 5:
            print("Too few rated coffee for person " + str(personId) + ". We skip this person.")
            continue
        else:
            print("Working on person " + str(personId))
            #get recommendations
            recommendation = getrecommend(personData,testingData,XColumns,dummyColumns,YColumn)
            personIdList += [personId] * 3
            coffeeNameList += testingData.loc[recommendation["rowIds"]]["coffeeName"].values.tolist()
            predictedRatingList += recommendation["newRatings"]
    #print recommendations
    for i in range(len(personIdList)):
        print(str(personIdList[i]) + " " + str(coffeeNameList[i]) + " " + str(int(round(predictedRatingList[i]))))
    recommendations = {}
    recommendations["personId"] = personIdList
    recommendations["coffeeName"] = coffeeNameList
    recommendations["rating"] = predictedRatingList
    recommendations = pd.DataFrame(recommendations)
    recommendations.rating = recommendations.rating.round()
    return(recommendations)

#define the function to predict the recommended coffee
def getrecommend(personData,testingData,XColumns,dummyColumns,YColumn):
    #clean training data
    trainingData = gettraining(personData,XColumns,dummyColumns,YColumn)
    #get the best random forest model by 5-fold CV
    [bestDepth,bestNumTree] = RFCV(trainingData,YColumn,k = 5,nTreeInitial = 50,maxDepth = 10,maxNumTrees = 100)
    bestParameter = [bestDepth,bestNumTree]
    #clean testing data
    testingData = gettesting(testingData,XColumns,dummyColumns,dropNA=False,shuffle=False)
    #predict by the best random forest model
    dataOutput = bestfit(testingData,trainingData,parameter = bestParameter,YColumn=YColumn)
    #sort by rating and get the recommended 3 coffees
    dataOutput = dataOutput.sort_index(by=["rating"],ascending=[True])
    recommendation = {}
    recommendation["rowIds"] = dataOutput.iloc[-3:,].index.tolist()
    recommendation["newRatings"] = dataOutput.iloc[-3:,]["rating"].values.tolist()
    return(recommendation)

#define the function to get training data
def gettraining(data,XColumns,dummyColumns,YColumn = [],dropNA = True,shuffle = True):
    trainingData = data.copy()
    trainingData = trainingData[XColumns+YColumn]
    if dropNA == True:
        #drop Na values if necessary
        trainingData = trainingData.dropna()
    if shuffle == True:
        #shuffle data if necessary
        trainingData = trainingData.reindex(np.random.permutation(trainingData.index))
    #convert categorical data to dummy variables
    if dummyColumns != []:
        trainingData = getdummy(trainingData,dummyColumns)
    return(trainingData)

#define the function to get testing data
def gettesting(data,XColumns,dummyColumns,YColumn = [],dropNA = True,shuffle = True):
    testingData = data.copy()
    testingData = testingData[XColumns+YColumn]
    if dropNA == True:
        #drop Na values if necessary
        testingData = testingData.dropna()
    if shuffle == True:
        #shuffle data if necessary
        testingData = testingData.reindex(np.random.permutation(testingData.index))
    #convert categorical data to dummy variables
    if dummyColumns != []:
        testingData = getdummy(testingData,dummyColumns)
    return(testingData)

#define the function to convert categorical data to dummy variables
def getdummy(rawData,categories):
    data = rawData.copy()
    for category in categories:
        columns = list(data.columns.values)
        columnValues = set(data[category])
        dummy = pd.get_dummies(data[category],prefix=category)
        if dummy.shape[1] > 1:
            columns.remove(category)
            data = data[columns].join(dummy.ix[:,1:])
        elif dummy.shape[1] == 1:
            columns.remove(category)
            data = data[columns].join(dummy)
    return(data)

#define the function to calculate the random forest CV error, k = 5 for default
def RFCV(data,YColumn,k = 5,nTreeInitial = 50,maxDepth = 5,maxNumTrees = 200):
    #convert YColumn from a list to a string
    YColumn = YColumn[0]
    #make number of rows divisible by 5
    n = data.shape[0]/k*k
    data = data.iloc[range(n)]
    #set up the initial values for these two tuning parameters
    nCandidates = [2,5,20,50,100,200,300,400,500,1000]
    numTrees = nCandidates[:nCandidates.index(maxNumTrees)+1]
    depths = range(1,maxDepth+1)
    #first tune depth with initial number of trees
    depthErrors = []
    for d in depths:
        #begin k-fold CV
        CVtestMSE = 0
        for i in range(k):
            #get training data & test data split
            testingData = data.iloc[range(i*n/k,(i+1)*n/k)]
            trainingData = data.iloc[range(0,i*n/k)+range((i+1)*n/k,n)]
            #get test & training & target
            training = trainingData.drop(YColumn,axis=1)
            target = trainingData[YColumn]
            testing = testingData.drop(YColumn,axis=1)
            #get model
            model = RandomForestRegressor(n_estimators=nTreeInitial,max_depth=d,max_features="sqrt")
            model = model.fit(training,target)
            #evaluate model and compute test error
            pred = np.array(model.predict(testing))
            testY = np.array(testingData[YColumn])
            CVtestMSE = CVtestMSE + np.linalg.norm(pred-testY)
        #append test errors
        depthErrors.append(CVtestMSE)
    #get the best maxDepth
    bestDepth = depths[depthErrors.index(min(depthErrors))]
    #then tune number of trees
    nErrors = []
    for numTree in numTrees:
        #begin k-fold CV
        CVtestMSE = 0
        for i in range(k):
            #get training data & test data split
            testingData = data.iloc[range(i*n/k,(i+1)*n/k)]
            trainingData = data.iloc[range(0,i*n/k)+range((i+1)*n/k,n)]
            #get test & training & target
            training = trainingData.drop(YColumn,axis=1)
            target = trainingData[YColumn]
            testing = testingData.drop(YColumn,axis=1)
            #get model
            model = RandomForestRegressor(n_estimators=numTree,max_depth=bestDepth,max_features="sqrt")
            model = model.fit(training,target)
            #evaluate model and compute test error
            pred = np.array(model.predict(testing))
            testY = np.array(testingData[YColumn])
            CVtestMSE = CVtestMSE + np.linalg.norm(pred-testY)
        #append test errors
        nErrors.append(CVtestMSE)
    #get the best numTrees
    bestNumTree = numTrees[nErrors.index(min(nErrors))]
    return([bestDepth,bestNumTree])

#define the function to fit the best model to all coffees
def bestfit(testingData,trainingData,parameter,YColumn):
    #convert YColumn from a list to a string
    YColumn = YColumn[0]
    #make a copy
    data = testingData.copy()
    #match all training features with testing data
    XColumns = list(trainingData.columns.values)
    #exclude the response variable
    XColumns.remove(YColumn)
    data = data[XColumns]
    #fit the best model and make prediction
    #get parameters
    bestDepth = parameter[0]
    numTree = parameter[1]
    #get test & training & target
    training = trainingData.drop(YColumn,axis=1)
    target = trainingData[YColumn]
    #fit
    model = RandomForestRegressor(n_estimators=numTree,max_depth=bestDepth,max_features="sqrt")
    model = model.fit(training,target)
    #predict
    pred = model.predict(data)
    testingData[YColumn] = pred
    return(testingData)

#define the function to visualize the summary
def vissum(decafList,organicList,fairTradeList,adjectiveList,countryList):
    N = 3
    width = 0.35
    ind = np.arange(N)
    numTrues = (decafList.count(True),organicList.count(True),fairTradeList.count(True))
    numFalses = (decafList.count(False),organicList.count(False),fairTradeList.count(False))
    fig, ax = plt.subplots()
    ax.set_ylim([0,15000])
    rects1 = ax.bar(ind, numTrues, width, color='g')
    rects2 = ax.bar(ind + width, numFalses, width, color='b')
    ax.set_ylabel('Counts')
    ax.set_title('Coffee Type Summary')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(('Decaf', 'Organic', 'Fair Trade'))
    ax.legend((rects1[0], rects2[0]), ('True', 'False'))
    plt.show()

    #count frequencies
    adjectiveUnique = []
    adjectiveCount = []
    for adjective in set(adjectiveList):
        adjectiveUnique.append(adjective)
        adjectiveCount.append(adjectiveList.count(adjective))
    countryUnique = []
    countryCount = []
    for country in set(countryList):
        countryUnique.append(country)
        countryCount.append(countryList.count(country))

    adjectiveInfo = pd.Series(np.array(adjectiveCount),index=adjectiveUnique)
    fig, ax = plt.subplots()
    pos = np.arange(len(adjectiveUnique))+.5   # the bar centers on the y axis
    plt.barh(pos,adjectiveInfo.order(), align='center',alpha =0.5 )
    plt.yticks(pos, adjectiveInfo.order().index,fontsize=11)
    plt.xlabel('<-  fewer  <-     count     ->  more  ->')
    plt.title('Adjective Info')
    plt.show()

    countryInfo = pd.Series(np.array(countryCount),index=countryUnique)
    fig, ax = plt.subplots()
    pos = np.arange(len(countryUnique))+.5   # the bar centers on the y axis
    plt.barh(pos,countryInfo.order(), align='center',alpha =0.5 )
    plt.yticks(pos, countryInfo.order().index,fontsize=11)
    plt.xlabel('<-  fewer  <-     count     ->  more  ->')
    plt.title('Country Info')
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='KIXEYE Coffee Tasting')
    subparsers = parser.add_subparsers(dest='command', help='command')

    commands = ['parse', 'summarize', 'recommend']
    parsers = {
        c: subparsers.add_parser(c) for c in commands
    }

    parsers['parse'].add_argument('arg', help='coffee descriptive name')
    parsers['summarize'].add_argument('arg', help='input csv file',
                                      type=argparse.FileType('r'))
    parsers['recommend'].add_argument('arg', help='input csv file',
                                      type=argparse.FileType('r'))
    args = parser.parse_args()
    globals()[args.command](args.arg)


if __name__ == '__main__':
    main()
