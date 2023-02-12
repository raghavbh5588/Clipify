import pandas as pd
import numpy as np


# Generate a function that reads a file and seperates each row as it's own list of integers with values seperated by commas
def readfile(filename):
    '''
    Reads a file and seperates each row as it's own list of integers with values seperated by commas
    '''
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split(',') for line in lines]
        for line in lines:
            if line == ['']:
                lines.remove(line)

    return lines


def gettrans(timestamps, topic):

    indexes = [[] for i in topic]

    for i in range(len(topic)):
        for j in range(5,len(timestamps),9):
            if int(float(timestamps[j][0])) == int(topic[i]) or ( int(float(timestamps[j][0])) <= ((int(topic[i]))+15) and int(float(timestamps[j][0])) >= ((int(topic[i]))-15)):
                
                indexes.append([j-4,j-3,j-2,j-1,j,j+1,j+2,j+3,j+4])
                    
    return indexes


def partition(indexes,timestamps):
    '''
    Takes a section of the text from the begining of the topic (begts) and the end of the topic (endts)
    '''
    transitions =[[] for i in range(len(indexes))]
    transpara = ""
    transtime = 0
    value = 0

    
    for i in range(len(indexes)):
        transpara = ""
        for j in range(0,len(indexes[i])):

            value = indexes[i][j]
            temp = timestamps[value][1]
            transpara += temp + " "
            #print(transpara)
        for k in range(0,len(indexes[i])):
            temp = timestamps[value][0]
            transtime = temp
            #print(transtime)
        if transtime == 0:
            continue
        transitions[i].append(transtime)
        transitions[i].append(transpara)
        
    return transitions

def partitionSANS(indexes,timestamps):
    '''
    Takes a section of the text from the begining of the topic (begts) and the end of the topic (endts)
    '''
    transitions =[[] for i in range(len(indexes))]
    transpara = ""
    value = 0


    for i in range(len(indexes)):
        transpara = ""
        for j in range(0,len(indexes[i])):
            value = indexes[i][j]
            temp = timestamps[value][1]
            transpara += temp + " "
            #print(transpara)
        transitions[i].append(transpara)
        
    return transitions


def partitionCOMP(indexes,timestamps):
    '''
    Takes a section of the text from the begining of the topic (begts) and the end of the topic (endts)
    '''
    transitions =[[] for i in range(len(indexes))]
    transpara = ""
    value = 0


    for i in range(len(indexes)):
        transpara = ""
        if indexes[i] == False:
            continue
  
        for j in range(0,len(indexes[i])):
            value = indexes[i][j]

            temp = timestamps[value][1]
            transpara += temp + " "
            #print(transpara)
        transitions[i].append(transpara)
        
    return transitions


def compress(timestamps):

    indexes = [[] in range(0,len(timestamps))]
   
    for i in range(9,len(timestamps),9):
        
        indexes.append([i-4,i-3,i-2,i-1,i,i+1,i+2,i+3,i+4])
    return indexes


# Read the file and store the data in a list of lists
topics = readfile("/Users/johnsurette/ITI1122JAVA/Clipify/Kaggle_Data_Base/TimeStampsInSeconds.csv")

#Define the topic of interest
topicsnum = 2
# Set the episode row of the transcript
topic = topics[topicsnum]

timestamps = readfile("/Users/johnsurette/ITI1122JAVA/Clipify/Kaggle_Data_Base/transcripts/Transcript2.csv")


timeindexes = gettrans(timestamps,topic)

transitionsections = partition(timeindexes,timestamps)

transitionarray = pd.DataFrame(transitionsections)

transitionarray.dropna(inplace=True)

dataarray = partitionSANS(timeindexes,timestamps)
dataarray = pd.DataFrame(dataarray)
dataarray.dropna(inplace=True)

labels = []
for i in range(len(dataarray)):
        labels.append(1)

dataarray['Labels'] = labels
dataarray.to_csv("Transition" + str(topicsnum) + "SANS.csv", index = None)

labels = []
for i in range(len(transitionarray)):
        labels.append(1)

transitionarray['Labels'] = labels

transitionarray.to_csv("Transition" + str(topicsnum) + "WITH_TIMESTAMPS.csv", index = None)


# FOR REGULAR DATA:

dataarray = [[] for i in range(len(timestamps))]

for i in range(len(timestamps)):
    dataarray[i].append(timestamps[i][1])

indexes = compress(timestamps)

dataarray = partitionCOMP(indexes,timestamps)

dataarray = pd.DataFrame(dataarray)
dataarray.dropna(inplace=True)

labels = []
for i in range(len(dataarray)):
        labels.append(0)
    
dataarray['Labels'] = labels

dataarray.to_csv("RegularStrs" + str(topicsnum) + ".csv", index = None)
   







    