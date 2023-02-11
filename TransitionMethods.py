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

    return lines


def gettrans(timestamps, topic):

    indexes = [[] for i in topic]

    for i in range(len(topic)):
        for j in range(len(timestamps)):
            if int(float(timestamps[j][0])) == int(float(topic[i])) or ( int(float(timestamps[j][0])) <= ((int(float(topic[i])))+3) and int(float(timestamps[j][0])) >= ((int(float(topic[i])))-3)):

                indexes.append([j-3,j-2,j-1,j,j+1,j+2,j+3])
                j += 3 # skip the next 3 lines to avoid duplicates
    return indexes


def partition(indexes,timestamps):
    '''
    Takes a section of the text from the begining of the topic (begts) and the end of the topic (endts)
    '''
    transitions =[[] for i in range(len(indexes))]
    transpara = ""
    transtime = 0
    temp = ""
    
    for i in range(len(indexes)):
        
        for j in range(len(indexes[i])):
            value = indexes[i][j]
            
            temp = timestamps[value-3][1]
            transpara += temp + " "

            temp = timestamps[value-3][0]
            transtime = temp
            print(transtime)
            transitions[i].append(transtime)
            transitions[i].append(transpara)
    

    return transitions




topics = readfile('TimeStampsInSeconds.csv')

topic = topics[0]

timestamps = readfile('Transcript1.csv')


timeindexes = gettrans(timestamps,topic)


transitionsections = partition(timeindexes,timestamps)




    