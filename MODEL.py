import cohere
import numpy as np
import numpy.array_api as npa
from numpy import vectorize
import pandas as pd
co = cohere.Client('CP3qAhd01F0x9Y01BElLse0AgQ9yY3ISj2nW4CH0') # This is your trial API key
from cohere.classify import Example


examp = '/Users/johnsurette/ITI1122JAVA/Clipify/train_set/DATA.csv'

# Generate code that can read a csv file and make an arrau of the data
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

examples = readfile(examp)
examples = pd.DataFrame(examples)
examples = examples.to_numpy()
np.vectorize(Example)

testin = '/Users/johnsurette/ITI1122JAVA/Clipify/RegularStrs3.csv'
testing = readfile(testin)
testing = pd.DataFrame(testing)
testing = testing.to_numpy()



response = co.classify(
  model= "large",
  inputs= testing,
  examples= examples,
)

print(response.classifications)