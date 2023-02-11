import pandas as pd
import numpy
import os

os.chdir(r'C:\Users\ragha\Clipify\Kaggle_Data_Base')

i= 1

timestampsarray = []
timeInSeconds = []

while i <= 95:
    timestamps = pd.read_table("timestamps\Episode-"+ str(i) +".txt", encoding= 'unicode_escape', header = None)

    df = pd.DataFrame(timestamps)

    df = df[0].str.split(" ", n=1, expand=True)
    df = df[0].str.split(":", n=2, expand= True)
    df[0] = pd.to_numeric(df[0])
    df[1] = pd.to_numeric(df[1])
    df[2] = pd.to_numeric(df[2])


    df = 3600*df[0] + 60*df[1] + df[2]

    timestampsarray = df.to_numpy()
    timestampsarray = numpy.delete(timestampsarray, 0)
    timestampsarray = numpy.delete(timestampsarray, -1)


    timeInSeconds.__iadd__([timestampsarray])
    i = i + 1

FinalTimeStamps = pd.DataFrame(timeInSeconds)


FinalTimeStamps = FinalTimeStamps.tail(-1)

FinalTimeStamps.to_csv("TimeStampsInSeconds.csv", index = None)