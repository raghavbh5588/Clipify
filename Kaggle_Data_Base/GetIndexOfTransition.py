import pandas as pd
import numpy as np
import os

transitionPoints = []

os.chdir(r'C:\Users\ragha\Clipify\Kaggle_Data_Base')

TimeStampsInSeconds = pd.read_csv("TimeStampsInSeconds.csv")
Transcript = pd.read_csv("transcripts\Transcript1.csv", header= None)

TimeStamps = pd.DataFrame(TimeStampsInSeconds)
Transcript = pd.DataFrame(Transcript)


arrayTimeStamps = TimeStamps.to_numpy()


for value in TimeStamps.iloc[:1].values[0]:
    if np.isnan(value):
        break
    df_sort = Transcript.iloc[(Transcript[0]-int(value)).abs().argsort()[:2]]
    val = df_sort.index.tolist()
    transitionPoints.__iadd__(val)

del transitionPoints[::2]
print(transitionPoints)