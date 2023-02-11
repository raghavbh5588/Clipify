import pandas as pd
import numpy
i= 1

timestampsarray = []
timeInSeconds = []

while i <= 95:
    transcript = pd.read_table("Transcripts\Episode-"+ str(i) +".txt", encoding= 'unicode_escape', header = None)

    df = pd.DataFrame(transcript)

    df = df[0].str.split(" ", n=1, expand=True)
    df.to_csv("Transcripts\Transcript"+ str(i) +".csv", index = None, header= None)

    i = i + 1
