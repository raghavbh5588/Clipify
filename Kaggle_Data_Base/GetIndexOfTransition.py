import pandas as pd
import numpy as np

TimeStampsInSeconds = pd.read_csv("TimeStampsInSeconds.csv")
Transcript = pd.read_csv("transcripts\Transcript1.csv")

TimeStamps = pd.DataFrame(TimeStampsInSeconds)
Transcript = pd.DataFrame(Transcript)

print(TimeStamps)
print(Transcript)