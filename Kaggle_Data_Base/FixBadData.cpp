import pandas as pd
import numpy as np
import os
import regex as re

i=1
os.chdir(r"C:\Users\ragha\Clipify\Kaggle_Data_Base")

while i<= 95:
    data = open('transcripts\Episode-'+ str(i) +'.txt', encoding="utf8").read().replace('\n', ' ')

    parts = re.findall(r'\D+|\d*\.?\d+', data)

    parts = [''.join(parts[i:i+2]) for i in range(0, len(parts), 2)]

    df = pd.DataFrame(parts)

    df = df[0].str.split(" ", n=1, expand=True)

    print(df)

    df.to_csv("Transcripts\Transcript"+ str(i) +".csv", index = None, header= None)
    i = i+1